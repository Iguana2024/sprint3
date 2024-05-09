from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymongo
import redis
from pymongo import MongoClient
import hashlib
import datetime
import uuid


app = Flask(__name__)


mongo_client = MongoClient('mongodb://flask:flask@mongodb:27017/flask')
db = mongo_client['data_storage']
permissions = db['permissions']
rejections = db['rejections']



def test_mongo_connection():
    try:
        info = mongo_client.server_info()
        return True, info
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return False, str(err)



def get_user_decision(ip):
    if permissions.find_one({'IP': ip}):
        return 'granted'
    elif rejections.find_one({'hashed_ip': hashlib.sha256(ip.encode()).hexdigest()}):
        return 'rejected'
    else:
        return None

@app.route('/')
def index():
    user_decision = get_user_decision(request.remote_addr)
    if user_decision == 'granted':
        return redirect(url_for('granted_permission'))
    elif user_decision == 'rejected':
        return redirect(url_for('rejected_permission'))
    else:
        return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():
    existing_permission = permissions.find_one({'IP': request.remote_addr, 'description': 'Granted access'})
    if existing_permission:
        return redirect(url_for('granted_permission'))
    existing_reject = rejections.find_one({'hashed_ip': hashlib.sha256(request.remote_addr.encode()).hexdigest(), 'description': 'Granted reject'})
    if existing_reject:
        return redirect(url_for('rejected_permission'))
    if request.form.get('grant'):
        permission = {
            'ID': str(uuid.uuid4()),
            'IP': request.remote_addr,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'description': 'Granted access'
        }
        permissions.insert_one(permission)
        return redirect(url_for('granted_permission'))
    elif request.form.get('reject'):
        
        hashed_ip = hashlib.sha256(request.remote_addr.encode()).hexdigest()
        rejection = {
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'hashed_ip': hashed_ip,
            'ID': str(uuid.uuid4()),
            'description': 'Granted reject'
        }
        rejections.insert_one(rejection)
        return redirect(url_for('rejected_permission'))

@app.route('/erase_data')
def erase_data():
    rejections.delete_many({})
    permissions.delete_many({})
    return redirect(url_for('index'))


@app.route('/granted_permission')
def granted_permission():
    return render_template('granted_permission.html')

@app.route('/rejected_permission')
def rejected_permission():
    return render_template('rejected_permission.html')

@app.route('/get_data')
def get_data():
    permission_data = list(permissions.find({}, {'_id': 0}))
    rejection_data = list(rejections.find({}, {'_id': 0}))
    return jsonify(permission_data=permission_data, rejection_data=rejection_data)




@app.route('/db')
def db():
    success, info = test_mongo_connection()
    if success:
        return f'MongoDB Server Info: {info}'
    else:
        return f'Failed to connect to MongoDB: {info}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
