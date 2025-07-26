import csv
import os
import sys

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

def get_writer(file_path, fieldnames):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', file_path)
    try:
        file = open(file_path, mode='w', newline='', encoding='utf-8')
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        return writer
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)