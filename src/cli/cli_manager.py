from cli.cli_interface import show_menu

from service.customer_service import CustomerService


def manage_menu():
    options = ["Print customer list", "Create a Customer",
                            "Check existing Book",
                            "Search Customer information by name",
                            "Update Customer",
                            "Save Customer to file",
                            "Print customer list from the file",
                            "Quit"]
    option = show_menu(options)
    customer_service = CustomerService()
    while 0 < option < len(options):
        match option:
            case 1:
                customer_service.print_all_customers()
                option = show_menu(options)
            case 2:
                result = customer_service.create_customer()
                if result:
                    print("Create successful")
                    option = show_menu(options)
                else:
                    print("Create fail")
                    option = show_menu(options)
            case default:
                print("Quit")
                break