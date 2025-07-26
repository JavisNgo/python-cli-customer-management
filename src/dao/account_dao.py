from dao.csv_handler import get_reader

account_file_path = "data/account.csv"

def get_accounts():
    accounts = {}
    reader = get_reader(account_file_path)
    for row in reader:
        accounts[row['username']] = row['password']
    return accounts