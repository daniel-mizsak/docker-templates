import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "some_db"
username = "postgres"
pwd = "postgres"
port_id = 5432

conn = None

try:
    with psycopg2.connect(
        host=hostname, dbname=database, user=username, password=pwd, port=port_id
    ) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM employee")
            for record in cur.fetchall():
                print(record["name"], record["salary"])


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
