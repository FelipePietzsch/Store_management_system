import product
import store
import menu

def start(store):
    """Asks user for input and executes funktion from dictionary

    Args:
        store(class Store): contains all data and funktions from the 'Store' class
    """
    UI = menu.User_Interface(store)
    menu_funtions = {
        1: UI.list_all_products,
        2: UI.total_amount,
        3: UI.create_order,
        4: UI.quit
    }

    while True:
        try:
            print_menu()
            user_input = int(input("Please choose a number: "))
            check_user_input(user_input)
            menu_funtions[user_input]()
        except ValueError as e:
            print(e)


def print_menu():
    """Displays UI menu"""
    print("\n\tStore Menu\n"
          "\t----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")


def check_user_input(user_input):
    """Checks, if user_input for UI Menu, is in valid range"""
    if 0 > user_input > 5:
        raise ValueError("Input must be a number between 1 and 4!")



def main():
    """Contais all products, initialiates the instance 'best_buy' from the Store class and starts the best_buy 'shop'"""
    product_list = [
        product.Product("MacBook Air M2", price=1450, quantity=100),
        product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        product.Product("Google Pixel 7", price=500, quantity=250)
        ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()


