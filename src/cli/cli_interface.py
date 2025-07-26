import argparse

def show_menu(options):
    for i in range(len(options)):
        print(f"{i + 1} - {options[i]}")
    return int(input("Choose an option:"))


def parse_arguments():
    parser = argparse.ArgumentParser(description="User Management CLI")
    parser.add_argument("-u", "--username", required=True, help="Username")
    parser.add_argument("-p", "--password", required=True, help="Password")
    return parser.parse_args()