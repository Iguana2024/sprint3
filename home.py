import time
from flask import Flask
import redis
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

mongo_client = MongoClient('mongodb://flask:flask@mongodb:27017/flask')

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def test_mongo_connection():
    try:
        info = mongo_client.server_info()
        return True, info
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return False, str(err)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello from root. Redis hits: {count}'

@app.route('/db')
def db():
    success, info = test_mongo_connection()
    if success:
        return f'MongoDB Server Info: {info}'
    else:
        return f'Failed to connect to MongoDB: {info}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
