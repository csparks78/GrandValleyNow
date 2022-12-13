import logging
import os
import psycopg
from psycopg.errors import ProgrammingError
def main():

    # Connect to CockroachDB
    with psycopg.connect(os.environ["DATABASE_URL"], application_name="$ testInsert") as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO events(eventName,tags,link,address,city,state,zip,lat,long,day,month,year,time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            ("TestEvent", "test,event","www.testevent.com","1001 S. Test Street", "Grand Junction", "CO", "81501", 78.124124, 73.124124, 8, 11, 2022, "8:44 AM"))
            cur.execute("SELECT * FROM events")
            cur.fetchone()

            for record in cur:
                print(record)

            conn.commit()

           


if __name__ == "__main__":
    main()
