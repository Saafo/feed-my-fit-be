# OTHER SETTINGS
import json

config = {}
with open('./config.json') as f:
    config = json.load(f)

DEBUG = config['DEBUG'] == "True"
PORT = config['PORT']
HOST = config['HOST']
SECRET_KEY = config['SECRET_KEY']
