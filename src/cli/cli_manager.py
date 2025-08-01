from cli.cli_interface import show_menu

from service.customer_service import CustomerService


def manage_menu():
    options = ["Print customer list", "Create a Customer",
                            "Update Customer",
                            "Search Customer information by email",
                            "Delete Customer",
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
            case 3:
                result = customer_service.update_customer()
                if result:
                    print("Update successful")
                    option = show_menu(options)
                else:
                    print("Update fail")
                    option = show_menu(options)
            case 4:
                customer = customer_service.get_customer_by_email()
                if customer:
                    print(customer.__str__(),"\n")
                    option = show_menu(options)
                else:
                    print("Customer not found", "\n")
                    option = show_menu(options)
            case 5:
                result = customer_service.delete_customer()
                if result:
                    print("Delete successful")
                    option = show_menu(options)
                else:
                    print("Delete fail")
                    option = show_menu(options)
            case default:
                print("Quit")
                break