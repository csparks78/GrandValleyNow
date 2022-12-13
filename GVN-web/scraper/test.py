#file not needed, just testing

import json
import random


s = "university center"
test = "The main building is the University Center in the Mesa Colorado University"

def checker(s, ss):
    print("1. no changes")
    print("True") if s in ss else print("False")
    
    print("2. all lowercase")
    print("True") if s.lower() in ss.lower() else print("False")
    
checker(s, test)

f = json.load(open("scraper\\locations.json"))
print(random.choice(f['random']['coordinates']))

f = json.load(open("scraper\\data\\dataPresence.json"))
for e in f:
    if e['coordinates'] == None:
        e['coordinates'] = "random"
    print(e)