from datetime import datetime

import dao.customer_dao as customer_dao

from model.customer_model import Customer

from util.util import is_valid_email


class CustomerService:
    pass
    def __init__(self):
        self.customers = {}

    def print_all_customers(self):
        self.customers = customer_dao.get_customers()
        print("=======================================")
        for customer in self.customers:
            print(customer.__str__())
        print('\n')

    def create_customer(self):
        customer_model = Customer
        print("Enter customer information:")
        while True:
            username = input("Username: ")
            if any(customer.username == username for customer in self.customers):
                print(f"Error: Username '{username}' already exists.")
            else:
                customer_model.username = username
                break
        while True:
            full_name = input("Full name: ")
            if full_name.strip() == "":
                print("Error: Full name cannot be empty.")
            else:
                customer_model.full_name = full_name
                break
        while True:
            email = input("Email: ")
            if any(customer.email == email for customer in self.customers):
                print(f"Error: Email '{email}' already exists.")
            if not is_valid_email(email):
                print(f"Error: Email '{email}' is invalid format.")
            else:
                customer_model.email = email
                break
        while True:
            year_of_birth = int(input("Year of Birth: "))
            current_year = datetime.now().year
            if year_of_birth < 1900 or year_of_birth > current_year:
                print("Error: Invalid year of birth.")
            else:
                customer_model.year_of_birth = year_of_birth
                break
        result = customer_dao.create_customer(customer_model)
        return result