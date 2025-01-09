import product

class Store:
    def __init__(self, products:list):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity


    def get_all_products(self):
        all_active_products = []
        for product in self.products:
            if product.active:
                all_active_products.append(product)

        return all_active_products


    def order(self, order_list) -> float:
        total_price = 0

        for product in order_list:
            product_name = product[0]
            quantity = product[1]

            total_price += product_name.price * quantity

        return total_price

product_list = [product.Product("MacBook Air M2", price=1450, quantity=100),
                product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                product.Product("Google Pixel 7", price=500, quantity=250),
                ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products[0], 1), (products[1], 2)]))








