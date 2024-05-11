from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
import pymongo
from pymongo import MongoClient
import hashlib
import datetime
import uuid
import os
import redis
import json  

# Initialize Flask app
app = Flask(__name__)

# Setup for Redis and MongoDB remains the same
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_db = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)
mongo_client = MongoClient('mongodb://mongodb:27017/')
db = mongo_client['data_storage']
permissions = db['permissions']
rejections = db['rejections']

def test_mongo_connection():
    """
    Test connection to MongoDB server.
    Returns:
        bool: True if connection successful, False if not.
        str: Server information or error message.
    """
    try:
        info = mongo_client.server_info()
        return True, info
    except pymongo.errors.ServerSelectionTimeoutError as err:
        return False, str(err)
    
def hash_ip(ip):
    """
    This function hashes an IP address with salt using MD5 encryption.
    Args:
        ip (str): IP address that we need to hash.
    Returns:
        str: Hashed IP address.
    """
    salt = "5gz"
    hash_ip_salt = ip + salt
    hashed_ip = hashlib.md5(hash_ip_salt.encode()).hexdigest()
    return hashed_ip       

def check_user_permission(ip):
    """
    Checks if a user gave permission before based on their IP address 
    Args:
        ip (str): IP address of the user.
    Returns:
        dictionary: User permission record if found, None otherwise.
    """
    permission = permissions.find_one({'IP': ip})
    return permission

def check_user_rejection(ip):
    """
    Checks if a user gave rejection before based on their IP address 
    Args:
        ip (str): IP address of the user.
    Returns:
        dictionary: User rejection record if found, None otherwise.
    """
    hashed_ip = hash_ip(ip)
    rejection = rejections.find_one({'hashed_ip': hashed_ip})
    return rejection

def get_user_decision(ip):
    if check_user_permission(ip):
        return 'granted'
    elif check_user_rejection(ip):
        return 'rejected'
    else:
        return None

@app.route('/')
def index():
    """
    Redirects users based on their previous decision or renders the home page.
    Returns:
        Response: Redirects to 'granted_permission' or 'rejected_permission' or renders 'home.html'.
    """
    user_decision = get_user_decision(request.remote_addr)
    if user_decision == 'granted':
        return redirect(url_for('granted_permission'))
    elif user_decision == 'rejected':
        return redirect(url_for('rejected_permission'))
    else:
        return render_template('home.html')

#
@app.route('/process', methods=['POST'])
def process():
    """
    Processes a permission request and redirects accordingly.
    Returns:
        Response: Redirects to 'granted_permission' or 'rejected_permission'.
    """
    # index()
    ip = request.remote_addr
    existing_permission = check_user_permission(ip)
    if existing_permission:
        return redirect(url_for('granted_permission'))
    existing_reject = check_user_rejection(ip)
    if existing_reject:
        return redirect(url_for('rejected_permission'))
    if request.form.get('grant'):
        return process_grant_request(ip)
    elif request.form.get('reject'):
        return process_reject_request(ip)

def process_grant_request(ip):
    """
    Processes a request to grant access.
    Args:
        ip (str): IP address of the request.
    Returns:
        Response: Redirects to 'granted_permission'.
    """
    ip = request.remote_addr
    unique_id = str(uuid.uuid4())
    datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    permission_data = {
        'id': unique_id[:5],
        'ip': ip,
        'datetime': datetime_now,
        'description': 'Granted access'
    }
    permissions.insert_one({
        'ID': unique_id,
        'IP': ip,
        'datetime': datetime_now,
        'description': 'Granted access'
    })
    redis_db.set(f"Granted:{unique_id}:{ip}:{datetime_now}", json.dumps(permission_data))
    return redirect(url_for('granted_permission'))

def process_reject_request(ip):
    """
    Processes a request to reject access.
    Args:
        ip (str): IP address of the request.
    Returns:
        Response: Redirects to 'rejected_permission'.
    """
    unique_id = str(uuid.uuid4())
    hashed_ip = hash_ip(ip)
    datetime_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rejection_data = {
        'id': unique_id[:5],
        'hashed_ip': hashed_ip,
        'datetime': datetime_now,
        'description': 'Rejected access'
    }
    rejections.insert_one({
        'ID': unique_id,
        'hashed_ip': hashed_ip,
        'datetime': datetime_now,
        'description': 'Rejected access'
    })
    redis_db.set(f"Rejected:{unique_id}:{hashed_ip}:{datetime_now}", json.dumps(rejection_data))
    return redirect(url_for('rejected_permission'))

@app.route('/erase_data')
def erase_data():
    """
    Remove user data based on their decision.
    This function retrieves the user's IP address, hashes it, and determines their previous decision (granted or rejected).
    If the user was granted access, it deletes their permission record from the permissions collection in the database
    and removes corresponding keys from the Redis database.
    If the user was rejected, it deletes their rejection record from the rejections collection in the database
    and removes corresponding keys from the Redis database.
    If there is no previous decision recorded, it simply returns without performing any action.
    Finally, it redirects the user to the home page.
    Returns:
        Response: Redirects the user to the home page.
    """
    ip = request.remote_addr
    hashed_ip = hash_ip(ip)
    user_decision = get_user_decision(ip)

    if user_decision == 'granted':
        keys = redis_db.keys(f"Granted:*:{ip}:*")
        permissions.delete_many({'IP': ip})
    elif user_decision == 'rejected':
        keys = redis_db.keys(f"Rejected:*:{hashed_ip}:*")
        rejections.delete_many({'hashed_ip': hashed_ip})
    else:
        keys = []
    for key in keys:
        redis_db.delete(key)
    return redirect(url_for('index'))

@app.route('/granted_permission')
def granted_permission():
    return render_template('granted_permission.html')

@app.route('/rejected_permission')
def rejected_permission():
    return render_template('rejected_permission.html')

@app.route('/get_data')
def get_data():
    """
    Retrieve user data based on their decision.
    This function retrieves the user's IP address, hashes it, and determines their previous decision (granted or rejected).
    If the user was granted access, it retrieves permission data from the permissions collection in the database
    based on their IP address.
    If the user was rejected, it retrieves rejection data from the rejections collection in the database
    based on the hashed IP address.
    Finally, it returns a JSON response containing the retrieved permission and rejection data.
    Returns:
        Flask response: JSON response containing permission and rejection data.
    """
    ip = request.remote_addr
    hashed_ip = hash_ip(ip)
    user_decision = get_user_decision(ip)
    if user_decision == 'granted':
        permission_data = list(permissions.find({'IP': ip}, {'_id': 0}))
        rejection_data = []
    elif user_decision == 'rejected':
        permission_data = []
        rejection_data = list(rejections.find({'hashed_ip': hashed_ip}, {'_id': 0}))
    return jsonify(permission_data=permission_data, rejection_data=rejection_data)

@app.route('/form')
def form():
     return render_template('form.html')

@app.route('/db')
def db():
    success, info = test_mongo_connection()
    if success:
        return f'MongoDB Server Info: {info}'
    else:
        return f'Failed to connect to MongoDB: {info}'

if __name__ == '__main__':
    app.run(host='0.0.0.0') 