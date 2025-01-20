class Store:
    """contains all data and functions to interact with an store object"""
    def __init__(self, products:list):
        self.products = products


    def add_product(self, product):
        """adds a new product to the store"""
        self.products.append(product)


    def remove_product(self, product):
        """removes a product from the store (!the product will be deleted, not deactivated)"""
        self.products.remove(product)


    def get_total_quantity(self):
        """returns the total amout of products in the store"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity


    def get_all_products(self):
        """returns all active products"""
        all_active_products = []
        for product in self.products:
            if product.active:
                all_active_products.append(product)

        return all_active_products


    def order(self, order_list) -> float:
        """creates a list with all products, who where made in a order in menu.py: 60; than executes the '.buy()' method from product.py: 41"""
        total_price = 0

        for product in order_list:
            try:
                product_name = product[0]
                quantity = product[1]
                product_name.buy(quantity)

                total_price += product_name.price * quantity
            # gets Error raise form product.py: 38
            except ValueError as e:
                print(e)

        return total_price






