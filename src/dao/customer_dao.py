from dao.csv_handler import get_reader
from model.customer_model import Customer
from dao.csv_handler import get_writer
import util.util as util

customer_file_path = "data/customer.csv"
general_password_customer = 1

def get_customers():
    reader = get_reader(customer_file_path)
    customers = [Customer(
        row['username'],
        row['full_name'],
        row['year_of_birth'],
        row['password'],
        row['email'],
        row['create_at'],
        row['update_at']
    ) for row in reader]
    return customers

def create_customer(customer_model):
    fieldnames = ['username', 'full_name', 'year_of_birth', 'password', 'email', 'create_at', 'update_at']
    writer = get_writer(customer_file_path, fieldnames)
    writer.writerow({
        'username': customer_model.username,
        'full_name': customer_model.full_name,
        'year_of_birth': customer_model.year_of_birth,
        'password': util.hash_password(general_password_customer),
        'email': customer_model.email,
        'create_at': util.get_current_datetime(),
    })
    return True
