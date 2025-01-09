class User_Interface:
    def __init__(self, store):
        self.store = store

    # dafür sorgen, dass immer weiter nach produckten gesucht wird, bis keine iengabe mehr kommmt
    def get_order(self):
        order_list = []
        while True:
            try:
                product_index = int(input("Which product # do you want? "))
                product_name = self.store.products[product_index-1]
                quantity = int(input("What amount do you want? "))
                break # hier muss die schleife weitergehen
            except ValueError as e:
                print(e)
        if product_name == 0 or quantity == 0: # dass muss der break sein
            return None
        else:
            order_list.append((product_name, quantity))

        return order_list


    @staticmethod
    def quit():
        quit()

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




