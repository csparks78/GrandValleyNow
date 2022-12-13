#file depricated, not used anymore

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
class scrawler:
    #change the amount of events you want
    amount = 5
    events = []
    filteredWords = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

    def __init__ (self):
        print("setting up the driver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        scrawler.scrape(driver, scrawler.amount)

    def scrape(driver, amount):
        print("Switching to content view")
        driver.switch_to.default_content()

        print("switching to list view")
        driver.switch_to.frame("trumba.spud.0.iframe")
        driver.find_element(By.ID, "tab2").click()
        driver.switch_to.default_content()

        print("waiting for list view to load")
        time.sleep(3) #let the iframe load
        
        print("scraping the ")
        driver.switch_to.frame("trumba.spud.2.iframe")
        table = driver.find_element(By.CLASS_NAME, "twTable")
        
        rows = table.find_elements(By.TAG_NAME, "tr")
        print("rows length:",len(rows))

        _event = []
        for i in range(1, len(rows)-1):
            rowText = rows[i].text.strip()
            if rowText != "" and not tools.wordsInString(scrawler.filteredWords, rowText):
                _event.append(rowText)
                if(len(_event) >= 2):
                    scrawler.events.append(_event)
                    _event = []

        if(len(scrawler.events) < amount):
            print("Events:", len(scrawler.events))
            scrawler.nextPage(driver)
        else:
            print("Events:", len(scrawler.events))
            _events = parser.array(scrawler.events)
            print(_events)
            with open('./scraper/events.json', 'w', encoding='utf-8') as f:
                json.dump(_events, f, ensure_ascii=False, indent=4)
            print("Events saved to events.json in the same folder.")
            print("Done.")
            quit()

    def nextPage(driver):
        driver.switch_to.default_content()
        driver.switch_to.frame("trumba.spud.2.iframe")
        driver.find_element(By.XPATH, "/html/body/form/div[3]/div[3]/span[1]/a[2]").click()
        scrawler.scrape(driver, scrawler.amount)
        
class parser:
    def __init__(self):
        pass
    
    def JSON(JSONFile):
        pass

    def array(array):
        _array = []
        for item in array:
            _info = tools.stringToInfo(item[0])
            print(_info)
            _desc = item[1]
            item = _info
            item["desc"] = _desc
            _array.append(item)
        return _array
        
class tools:
    def __init__(self):
        pass

    def wordsInString(wordList, string):
        for word in wordList:
            if word in string:
                return True
        return False

    def stringToInfo(string):
        words = string.split()
        _dotw = words[0]
        _date = words[1:3]
        _stime = words[4]
        _ftime = ""
        for l in words[6]:
            _ftime += l
            if l == "p" or l == "a": break
        _loc = words[6:]
        for l in _loc[0]:
            if l == "p" or l == "a":
                _loc[0] = _loc[0][1:]
                break
            else: _loc[0] = _loc[0][1:]
        info = {
            "dotw":_dotw,
            "date":_date,
            "stime":_stime,
            "ftime":_ftime,
            "loc":_loc
        }
        return info

url = "https://www.coloradomesa.edu/calendar/index.html"
colorado = scrawler()