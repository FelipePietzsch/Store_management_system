class Product:
    def __init__(self, name:str, price:float, quantity:int, active:bool=True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active


    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        total_price = self.price * quantity

        try:
            self.reduce_quantity(quantity)
            return f"Total Price: {total_price}, new product quantiy: {self.quantity}"
        except ValueError as e:
            print(e)


    def reduce_quantity(self, quantity):
        if self.quantity < quantity:
            raise ValueError(f"Not enough {self.name}´s in stock. Only {self.quantity} {self.name}´s left.")
        else:
            self.quantity -= quantity

        if self.quantity == 0:
            self.active = False




