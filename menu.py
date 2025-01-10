from ast import Index


class User_Interface:
    def __init__(self, store):
        self.store = store


    @staticmethod
    def quit():
        quit()


    def get_order(self):
        order_list = []
        while True:
            try:

                product_index = input("Which product # do you want? ")
                quantity = input("What amount do you want? ")

                if len(product_index) == 0 or len(quantity) == 0:
                    return order_list

                product_index = int(product_index)
                quantity = int(quantity)

                product_name = self.store.get_all_products()[product_index - 1]
                order_list.append((product_name, quantity))

            except ValueError as e:
                print(e)

            except IndexError as e:
                print(e)


    def list_all_products(self):
        all_active_products = self.store.get_all_products()
        product_num = 0

        print("------")
        for product in all_active_products:
            product_num += 1
            print(f"{product_num}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        print("------")


    def total_amount(self):
        total_amount = self.store.get_total_quantity()

        print(f"Total of {total_amount} items in store")


    def create_order(self):
        self.list_all_products()

        order_list = self.get_order()

        if type(order_list) is list:
            total_price = self.store.order(order_list)

            print("********")
            print(f"Order made! Total payment: ${total_price}")




