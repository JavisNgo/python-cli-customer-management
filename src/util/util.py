import random
import string
import bcrypt
import datetime
import re


def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return str(hashed_password)

def get_current_datetime():
    return datetime.datetime.now()

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string