from programm_modules.promotion import Promotion

class User_Interface:
    """class contains all data and functions to interact, with the referenced 'class Store', via the UI"""
    def __init__(self, store):
        self.store = store

    @staticmethod
    def quit():
        """Quits programm"""
        quit()

    def get_order(self):
        """Takes the order from User and checks if it is valid"""
        order_list = []
        print("Type in your order. For ending order type in 'empty_text' two times")
        while True:
            try:
                product_index = input("Which product # do you want?: ")
                quantity = input("What amount do you want?: ")

                # if user_input is an empty string, user gets back an empty list
                if len(product_index) == 0 or len(quantity) == 0:
                    return order_list

                product_index = int(product_index)
                quantity = int(quantity)

                product_name = self.store.get_all_products()[product_index - 1]
                order_list.append((product_name, quantity))

            except ValueError:
                print("Invalid input. Please enter valid numbers for product and quantity.")

            except IndexError as e:
                print(e)

    def list_all_products(self):
        """Displays all active products in the 'class Store'"""
        all_active_products = self.store.get_all_products()
        product_num = 0

        print("------")
        for product in all_active_products:
            product_num += 1

            if isinstance(product.promotion_type, Promotion):
                print(f"{product_num}. {product.name}, Price: {product.price}, Quantity: {product.quantity}, {product.promotion_type.promotion_type}")
            else:
                print(f"{product_num}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        print("------")

    def total_amount(self):
        """Displays the total amount of products in the 'class Store'"""
        total_amount = self.store.get_total_quantity()

        print(f"Total of {total_amount} items in store")

    def create_order(self):
        """Creates the Order from User, checks it validation and displays the final total_price"""
        self.list_all_products()

        order_list = self.get_order()

        if type(order_list) is list:
            total_price = self.store.order(order_list)

            print("********")
            print(f"Order made! Total payment: ${total_price}")

    def run(self):
        while True:
            print("\nWelcome to the Store!")
            # TODO nur objekte der Product class werden angezeigt
            # TODO promotion muss noch geprintet werden
            print("1. List all products")
            print("2. Place an order")
            print("3. Show total items in store")
            print("4. Quit")
            choice = input("Select an option: ")

            if choice == '1':
                self.list_all_products()
            elif choice == '2':
                self.create_order()
            elif choice == '3':
                self.total_amount()
            elif choice == '4':
                self.quit()
            else:
                print("Invalid option, please type in a valid number (1-4):")






