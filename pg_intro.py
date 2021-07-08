import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import psycopg2
from urllib.parse import urlparse

# You can create a database with:
# psql -c "CREATE DATABASE products;"

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database... (set environnment variable to connect)')
        url = urlparse(os.environ['DATABASE_URL']) #'postgresql://gitpod@localhost/products'
        conn = psycopg2.connect("host={} dbname={} user={}".format(url.hostname, url.path[1:] or os.environ['PGDATABASE'], url.username))

        # create a cursor
        cur = conn.cursor()

	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # list tables
        s = "SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public');"
        cur.execute(s)
        print('List of Tables: {}'.format(str(cur.fetchall())))

	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
