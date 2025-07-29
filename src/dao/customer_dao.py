import sys

from model.customer_model import Customer
import util.util as util

import dao.csv_handler as csv_handler

from dao.csv_handler import upload_data

customer_file_path = "data/customer.csv"
general_password_customer = '1'

def get_customers():
    reader = csv_handler.get_reader(customer_file_path)
    customers = [Customer(
        row['username'],
        row['full_name'],
        row['year_of_birth'],
        row['password'],
        row['email'],
        row['created_at'],
        row['updated_at']
    ) for row in reader]
    return customers

def create_customer(customer_model):
    fieldnames = ['username', 'full_name', 'year_of_birth', 'password', 'email', 'created_at', 'updated_at']
    try:
        customer_data = {
            'username': customer_model.username,
            'full_name': customer_model.full_name,
            'year_of_birth': customer_model.year_of_birth,
            'password': util.hash_password(general_password_customer),
            'email': customer_model.email,
            'created_at': util.get_current_datetime(),
            'updated_at': ''
        }
        upload_data(customer_file_path, fieldnames, customer_data)
        return True
    except Exception as e:
        print(f"Error creating customer {customer_model.username}: {str(e)}")
        return False
