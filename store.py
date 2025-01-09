class Store:
    def __init__(self, products:list):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
