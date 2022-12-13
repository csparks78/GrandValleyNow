import logging
import os
import psycopg
from psycopg.errors import ProgrammingError
def main():

    # Connect to CockroachDB
    with psycopg.connect(os.environ["DATABASE_URL"], application_name="$ createDB") as conn:
        with conn.cursor() as cur:
            cur.execute("""DROP TABLE IF EXISTS events""")
            cur.execute("""CREATE TABLE events(
            id serial PRIMARY KEY,
            eventName text,
            tags text,
            link text,
            address text,
            city text,
            state text,
            zip text,
            lat double precision,
            long double precision,
            day smallint,
            month smallint,
            year smallint,
            time text)""")
            conn.commit()

           


if __name__ == "__main__":
    main()
