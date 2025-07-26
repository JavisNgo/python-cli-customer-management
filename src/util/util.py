import hashlib
import datetime

def hash_password(password):
    password = hashlib.sha256(password).hexdigest()
    return password

def get_current_datetime():
    return datetime.datetime.now()