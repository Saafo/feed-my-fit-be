import json
import database
import flaskapp


def main():
    debug = True
    mybase = None
    mybase.cur = None
    if debug is False: #TODO delete
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

    flaskapp.flaskapp(mybase.cur)

    if debug is False: #TODO delete
        mybase.conn.close()

if __name__ == "__main__":
    main()