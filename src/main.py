from service.auth import login
from cli.cli_interface import parse_arguments
from dao.account_dao import get_accounts
from cli.cli_manager import manage_menu

def main():
    args = parse_arguments()
    accounts = get_accounts()
    if accounts:
        if login(args.username, args.password, accounts):
            print('Login Successful')
            manage_menu()
        else:
            print('Login Failed')
    else:
        print("No accounts available to validate login.")
if __name__ == '__main__':
    main()