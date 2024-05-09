import time
from flask import Flask
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

mongo_client = MongoClient('mongodb://flask:flask@mongodb:27017/flask')

def test_mongo_connection():
    try:
        info = mongo_client.server_info()
        return True, info
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return False, str(err)

@app.route('/')
def hello():
    return f'Hello from root.'

@app.route('/db')
def db():
    success, info = test_mongo_connection()
    if success:
        return f'MongoDB Server Info: {info}'
    else:
        return f'Failed to connect to MongoDB: {info}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
