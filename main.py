import json
import database
import flaskapp


def main():
    config = {}
    with open('./config.json') as f:
        config = json.load(f)
    
    username = config['database']['username']
    password = config['database']['password']
    basename = config['database']['basename']
    hostname = config['database']['hostname']
    port = config['database']['port']

    mybase = database.Postgres(username,password,basename,hostname,port)
    mybase.connect()
    mybase.cursor()
    try:
        flaskapp.flaskapp(mybase.cur, mybase.conn)
    finally:
        mybase.conn.close()

if __name__ == "__main__":
    main()