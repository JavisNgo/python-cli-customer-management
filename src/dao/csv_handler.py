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


def upload_data(file_path, fieldnames, data):
    backup_dir = os.path.join(generate_random_string(8), 'backup')
    os.makedirs(backup_dir, exist_ok=True)

    backup_file_path = os.path.join(backup_dir, os.path.basename(file_path))

    try:
        if os.path.exists(file_path):
            shutil.copy2(file_path, backup_file_path)

        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            file.write('\n')

        if os.path.exists(backup_file_path):
            try:
                os.remove(backup_file_path)
            except PermissionError as pe:
                print(f"Permission Error: {pe}")

    except Exception as e:
        print(f"Error writing to CSV file: {str(e)}")
        if os.path.exists(backup_file_path):
            try:
                shutil.move(backup_file_path, file_path)
                print(f"Restored original file from backup.")
            except Exception as restore_error:
                print(f"Error when restoring files from backup: {str(restore_error)}")
        else:
            print("No backup file found to restore.")