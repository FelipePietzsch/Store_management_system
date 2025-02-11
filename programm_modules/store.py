class Store:
    """contains all data and functions to interact with an store object"""
    def __init__(self, products:list):
        self.products = products # list of classes of Product


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
            total_quantity += product.quantity()

        return total_quantity


    def get_all_products(self):
        """returns all active products"""
        all_active_products = []
        for product in self.products:
            if product.active:
                all_active_products.append(product)

        return all_active_products


    def order(self, order_list) -> float:
        """creates a list with all products, who where made in a order in menu.py: 60; than executes the '.buy()' method from oder_obj.py: 41"""
        total_price = 0

        for index, oder_obj in enumerate(order_list):
            # oder_obj is also a list/tuple
            try:
                product_obj = oder_obj[0]
                quantity = oder_obj[1]


                total_price += product_obj.buy(quantity)

            # gets Error raise form oder_obj.py: 38
            except ValueError as e:
                print(e)

        return total_price






