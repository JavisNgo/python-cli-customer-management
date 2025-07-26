def login(username, password, accounts):
    return username in accounts and accounts[username] == password