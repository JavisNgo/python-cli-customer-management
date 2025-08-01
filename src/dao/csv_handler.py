import csv
import os
import shutil
import sys

from util.util import generate_random_string


def get_reader(file_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', file_path)
    try:
        file = open(file_path, mode='r', newline='', encoding='utf-8')
        reader = csv.DictReader(file)
        return reader
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

def get_writer(file_path, fieldnames=None):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', file_path)
    try:
        file = open(file_path, mode='w', newline='', encoding='utf-8')
        writer = csv.DictReader(file)
        return writer
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

def upload_data(file_path, fieldnames, data):
    backup_file_path = ''
    try:
        backup_file_path = create_backup(file_path)

        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)

        commit(backup_file_path)
    except Exception as e:
        roll_back(backup_file_path, file_path)

def update_data_in_file(file_path, fieldnames, new_data):
    backup_file_path = create_backup(file_path)
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_data)
        commit(backup_file_path)
    except Exception as e:
        roll_back(backup_file_path, file_path)

def create_backup(file_path):
    backup_dir = os.path.join('data', 'backup')
    os.makedirs(backup_dir, exist_ok=True)

    backup_file_path = os.path.join(backup_dir, os.path.basename(generate_random_string(8)))
    if os.path.exists(file_path):
        shutil.copy2(file_path, backup_file_path)
        return backup_file_path
    else:
        return Exception

def commit(file_path):
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except PermissionError as pe:
            print(f"Permission Error: {pe}")
            sys.exit(1)

def roll_back(backup_file_path, file_path):
    if os.path.exists(backup_file_path):
        try:
            shutil.move(backup_file_path, file_path)
            print(f"Restored original file from backup.")
        except PermissionError as pe:
            print(f"Permission Error: {pe}")
            sys.exit(1)
    else:
        print("No backup file found to restore.")