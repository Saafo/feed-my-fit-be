# This file is about connecting the database
import psycopg2

class Postgres:
    username = ""
    password = ""
    basename = ""
    hostname = ""
    port = ""
    conn = None
    cur = None

    def __init__(self, user, passw, data, host, port):
        self.username = user
        self.password = passw
        self.basename = data
        self.hostname = host
        self.port = port

    def connect(self):
        self.conn = psycopg2.connect(database=self.basename, user=self.username, password=self.password, host=self.hostname, port=self.port)

    def cursor(self):
        self.cur = self.conn.cursor()
