# todo:
# redo DCLtime to try.catch
# improve the algorithm looking for coordinates

# instruction how to make the scraper match your needs on the site
# change the ids of the items and buttons to change the site if necessary
# change the itemsToInfo method to match the desired indexes

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

class scrawler:
    #change the amount of events you want (0 for all)
    amount = 0
    #Time needed to DomContentLoaded
    DCLtime = 20
    events = []
    parsedEvents = []

    def __init__ (self, url="https://coloradomesa.presence.io/events/list"):
        """initialize the scraper of CMU and opens the chrome driver (chrome needs to be installed)

        Args:
            url (string): the url of the cmu calendar (list view)
        """
        print("setting up the driver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        #wait for the page to load
        time.sleep(scrawler.DCLtime)
        #start scrawling
        scrawler.scrape(driver, scrawler.amount)

    def scrape(driver, amount):
        """scrape the events on the current page and if neccesary move to another (nextPage())

        Args:
            driver (driver): chrome driver declared in the __init__
            amount (int): amount of events you want to scrape
        """
        print("waiting for content to load")
        time.sleep(0.5)

        #scrape the list
        print("scraping the page")
        table = driver.find_element(By.CLASS_NAME, "table")
        totalEventAmount = driver.find_element(By.XPATH, "/html/body/cih-student/div[2]/ng-outlet/events/ng-outlet/events-list/div/dir-pagination-controls/ul/li[2]").text.split()
        totalEventAmount = int(totalEventAmount[len(totalEventAmount)-1])
        scrawler.events = table.find_elements(By.CLASS_NAME, "card")
        
        #every row of the list is added to _events and
        #then the tools.itemsToInfo() is used to parse
        #the events so they can be ready to be used in Json file
        _events = []
        for item in scrawler.events:
            _events.append(item.find_elements(By.TAG_NAME, "td"))
        _events = tools.itemsToInfo(_events)
        scrawler.parsedEvents += _events

        #if the amount of scraped events is smaller than the declared amount of events to scrap
        #go to the next page, otherwise stop scrpaing and save the events to the file
        if (amount == 0 and len(scrawler.parsedEvents) < totalEventAmount) or (amount > 0 and len(scrawler.parsedEvents) < amount):
            print("changing the page")
            scrawler.nextPage(driver)
        else:
            tools.parseNullLocation()
            with open('scraper\data\dataPresence.json', 'w', encoding='utf-8') as f:
                json.dump(scrawler.parsedEvents, f, ensure_ascii=False, indent=4)
            print("Data saved to 'DataPresence.json'")
            quit()
    
    #go to the next page by clicking the arrow at the bottom of the list
    def nextPage(driver):
        driver.find_element(By.XPATH, "/html/body/cih-student/div[2]/ng-outlet/events/ng-outlet/events-list/div/dir-pagination-controls/ul/li[4]").click()
        scrawler.scrape(driver, scrawler.amount)

class tools:
    def __init__(self):
        pass

    #makes sure that all the manually entered locations in "locations.json" are ready to be used
    def locationParser():
        for key in locationDict:
            _values = []
            for v in locationDict[key]['location']:
                _values.append(v.lower())
            locationDict[key]['location'] = _values
        with open('scraper\locations.json', 'w', encoding='utf-8') as f:
            json.dump(locationDict, f, ensure_ascii=False, indent=4)
        print("Locations parsed successfully to 'location.json'")
        
    #
    def locationToCoordinates(location):
        """uses the manually created file "locations.json" (same dir)
           to parse the location to it's coordinates on the map

        Args:
            location (string): location of the event got from the list

        Returns:
            list: [x, y]
        """
        for key in locationDict:
                _locs = location.split()
                for l in _locs:
                    l = l.lower()
                    if l in locationDict[key]['location']:
                        coordinates = locationDict[key]['coordinates']
                        return coordinates

    def parseNullLocation():
        _events = scrawler.parsedEvents
        for e in _events:
            if e['coordinates'] == None:
                e['coordinates'] = random.choice(locationDict['random']['coordinates'])
        scrawler.parsedEvents = _events

    #main functions 
    def itemsToInfo(items):
        """converts every row to the object in the list of events

        Args:
            items (list): unparsed rows scraped from the website

        Returns:
            list: parsed json object
        """
        _events = []
        for item in items:
            _event = []
            for i in range(len(item)-1):
                rowText = item[i].text.strip()
                _event.append(rowText)
            info = {
                "title":_event[0],
                "organization":_event[1],
                "dotw":"",
                "date":_event[3].strip()[0:10],
                "stime":_event[3].strip()[13:],
                "ftime":"",
                "loc":_event[2],
                "coordinates":tools.locationToCoordinates(_event[2])
            }
            _events.append(info)
        return _events

#first script looks if the locations.json are in the same dir to be later used
try:
    locationDict = json.load(open("scraper\\locations.json", "r"))
    tools.locationParser()
except:
    print("Couldn't locate 'locations.json'. Script quitting.")
    quit()

#initalize the scraper
colorado = scrawler()