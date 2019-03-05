import json
import psycopg2
from psycopg2.extras import RealDictCursor

db_host = "semicolons2019.c3xwj9uude6d.us-east-1.rds.amazonaws.com"
db_port = 5432
db_name = "Alexadb"
db_user = "sa"
db_pass = "root12345678"

def make_conn():
    conn = None
    conn = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (db_host, db_name, db_user, db_pass))
    return conn

def fetch_one_row_data(conn, query):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    raw = cursor.fetchall()
    for line in raw:
        return line[0]

def fetch_data(conn, query):
    result = {}
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    raw = cursor.fetchall()
    for line in raw:
        result[str(line[0])] = str(line[1])
    return result

def execute_query(conn, query):
    result = []
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return result

