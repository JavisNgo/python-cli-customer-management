import sys
from sys import flags

from model.customer_model import Customer
import util.util as util

import dao.csv_handler as csv_handler

customer_file_path = "data/customer.csv"
general_password_customer = '1'
fieldnames = ['username', 'full_name', 'year_of_birth', 'password', 'email', 'created_at', 'updated_at']

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
        csv_handler.upload_data(customer_file_path, fieldnames, customer_data)
        return True
    except Exception as e:
        print(f"Error creating customer {customer_model.username}: {str(e)}")
        return False

def update_customer(newdata, condition_value):
    flag = False
    try:
        reader = csv_handler.get_reader(customer_file_path)
        rows = list(reader)
        for row in rows:
            if row['email'] == condition_value:
                row.update(newdata)
                flag = True
                break
        if not flag:
            print(f"Not found customer by email with value: {condition_value}")
            return False
        csv_handler.update_data_in_file(customer_file_path, fieldnames, rows)
        return True

    except Exception as e:
        print(f"Error updating customer: {str(e)}")
        return False

def delete_customer(condition_value):
    try:
        reader = csv_handler.get_reader(customer_file_path)
        rows = list(reader)
        rows = [row for row in rows if row['email'] == condition_value]
        csv_handler.update_data_in_file(customer_file_path, fieldnames, rows)
        return True
    except Exception as e:
        print(f"Error deleting customer {condition_value}: {str(e)}")
        return False