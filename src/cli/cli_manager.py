from cli.cli_interface import show_menu
import service.customer_service as customer_service

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
                manage_menu()
                break
            case 2:
                customer_service.create_customer()
                break
            case default:
                print("Quit")
                break