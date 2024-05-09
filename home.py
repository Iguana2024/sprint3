from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import hashlib
import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['data_storage']
permissions = db['permissions']
rejections = db['rejections']
counter = db['counter']


if counter.count_documents({}) == 0:
    counter.insert_one({'count': 1})

def generate_id():
    count = counter.find_one()['count']
    counter.update_one({}, {'$inc': {'count': 1}})
    return count

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
    if request.form.get('grant'):
        permission = {
            'ID': generate_id(),
            'IP': request.remote_addr,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'description': 'Granted access'
        }
        permissions.insert_one(permission)
        return redirect(url_for('granted_permission'))
    elif request.form.get('reject'):
        hashed_ip = hashlib.sha256(request.remote_addr.encode()).hexdigest()
        rejection = {
            'hashed_ip': hashed_ip
        }
        rejections.insert_one(rejection)
        return redirect(url_for('rejected_permission'))

@app.route('/erase_data')
def erase_data():
    permissions.delete_many({})
    rejections.delete_many({})
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

if __name__ == '__main__':
    app.run(debug=True)