import logging
import os
import psycopg
from psycopg.errors import ProgrammingError
def main():

    # Connect to CockroachDB
    with psycopg.connect(os.environ["DATABASE_URL"], application_name="$ testRead") as conn:
        with conn.cursor() as cur:
            
            cur.execute("SELECT * FROM events")
            cur.fetchone()

            for record in cur:
                print(record)

            conn.commit()

           


if __name__ == "__main__":
    main()
