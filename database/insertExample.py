#Program to insert data into the database
import logging
import os
import psycopg
from psycopg.errors import ProgrammingError

def insertData(eventName, tags, link, address, city, state, zipcode, lat, longitude, day, month, year, time):
    with psycopg.connect(os.environ["DATABASE_URL"], application_name = "$ your_app_name_here") as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO events 
            (eventName,tags,link,address,city,state,zip,lat,long,day,month,year,time) VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(eventName, tags, link, address, city, state, zipcode, lat, longitude, day, month, year, time))

            conn.commit()


def main():
    eventName = "Test"
    tags = "cool, test"
    link = "thisisatest.com"
    address = "1002 N. Test Rd"
    city = "Grand Junction"
    state = "CO"
    zipcode = "81501"
    lat = 79.7900
    longitude = 12.1241
    day = 8
    month = 9
    year = 2022
    time = "8:59 AM"

    insertData(eventName, tags, link, address, city, state, zipcode, lat, longitude, day, month, year, time)


