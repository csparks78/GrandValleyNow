# Including the required things to run and use program
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
import json
import datetime

class scrawler:
    DCLtime = 20
    #The list of events that will be populated by the data grabbed
    events = []
    #To convert from writing to numbers for month
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    def __init__ (self, url):
        self.url = url
        print("setting up the driver")
        #Options is specifically to ave the browser window not show up while running
        options = Options()
        options.headless = True
        #setting up driver to
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(self.DCLtime)
        #Try to grab a element located on page if it is there continue if not move on will wait for 20 seconds as that is DCLTime
        try:
            WebDriverWait(driver, self.DCLtime).until(EC.presence_of_element_located((By.ID, "evvnt_discovery_iframe")))
            #Grabbing data from site and populating scrawler.events
            self.scrape(driver)
        except:
            print("LOADING TOOK TOO LONG")
        self.fix_months(self.events)
        for event in self.events:
            print(event)
        with open("grandjunction_events.json", "w") as final:
            #Get the events into json data to be sent to database
            json.dump(self.events, final)
        driver.quit()

    def scrape (self,driver):
        # If there is an iframe and you are using selenium must switch to it before you can 
        # access anything inside of it
        event_iframe = driver.find_element(By.ID, "evvnt_discovery_iframe")
        driver.switch_to.frame(event_iframe)
        # the name of the events on the website is 'c-card'
        # event_cards will grab all 30 events that are populated on page
        # can get more events just need to implement a scroll
        event_cards = driver.find_elements(By.CLASS_NAME, "c-card")
        num_cards = len(event_cards)
        # Must use an incrementer to keep track of which events you have clicked into
        for i in range (0, num_cards):
            if i != 0:
                # if i != 0 you need to switch back to iframe again to be able to click 'c-cards'
                event_iframe = driver.find_element(By.ID, "evvnt_discovery_iframe")
                driver.switch_to.frame(event_iframe)
                event_cards = driver.find_elements(By.CLASS_NAME, "c-card")
            # All 30 cards are in event cards; chose new one each time
            card = event_cards[i]
            # a dictionary to hold a single event that will then be appended to scrawler.events
            event = {}
            # Grabbing data from the card
            month_or_today =  card.find_element(By.CLASS_NAME, "text-xs").text
            event["month_or_today"] = month_or_today
            event["title"] = card.find_element(By.CLASS_NAME, "font-bold.line-clamp-2.leading-5").text
            list = card.find_element(By.CLASS_NAME, "font-light.text-gray-500.text-sm.leading-6.my-3.ml-5")
            list_elements = list.find_elements(By.TAG_NAME, "li")
            event["start_time"] = list_elements[0].text
            event["location_in_words"] = list_elements[1].text
            event["tag"] = card.find_element(By.CLASS_NAME, "flex-none").text
            # Sometimes if the event is on the day that scraper is running it will grab today
            # instead of grabbing some digit to represent day in that case we get the current day from system
            if(month_or_today.lower() != "today"):
                event["day_of_month"] = card.find_element(By.CLASS_NAME, "-mt-2").text
            else: 
                day = datetime.datetime.now()
                event["month_or_today"] = day.month
                event["day_of_month"] = day.day
            # Have to click in to the card to get the rest of the data from it
            card.click()
            try:
                # This data isn't shown on page where all the cards are
                # Must click into te cards to get access to this data again
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main-container']/main/div[2]/div[2]/div/ul/li[2]/div")))
                address = driver.find_element(By.XPATH, "//*[@id='main-container']/main/div[2]/div[2]/div/ul/li[2]/div").text
                split = address.split('\n')
                split = split[1:]
                event["address"] = split[0]
                event["city"] = split[1]
                event["zip"] = split[2]
                event["state"] = "CO"
                event_location_link = driver.find_element(By.XPATH, "//*[@id='main-container']/main/div[2]/div[2]/div/ul/li[2]/div/div[1]/a").get_attribute('href')
                split_event_location_link = event_location_link.split(',')
                found = split_event_location_link[len(split_event_location_link)-2].find("%20")
                if found != -1:
                    split_event_location_link[len(split_event_location_link)-2] = split_event_location_link[len(split_event_location_link)-2][:found] + split_event_location_link[len(split_event_location_link)-2][found+3:]
                coords = ["", ""]
                coords[0] = split_event_location_link[len(split_event_location_link)-2]
                coords[1] = split_event_location_link[len(split_event_location_link)-1]
                event["coordinates"] = coords
                event["link"] = driver.current_url
                # Easier to return back to place we started by getting the url again
                # Easier than using selenium's back feature
                driver.get(self.url)
                self.events.append(event)
            except TimeoutException:
                print("LOADING TOOK TOO LONG")
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "evvnt_discovery_iframe")))
            except TimeoutException:
                print("LOADING TOOK TOO LONG")
        driver.quit()    
    def fix_months(self,events):
        for event in events:
            if((event["month_or_today"]) in self.months):
                event["month_or_today"] = str(self.months.index(event["month_or_today"])+1)
                print(event["month_or_today"])

url = "https://www.gjsentinel.com/local-events/?_evDiscoveryPath=%3Ftowns%3DGrand%2BJunction"
gjsent = scrawler(url=url)
