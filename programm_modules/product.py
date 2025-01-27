from math import inf

class Product:
  """Contains all data and functions, to interact with a specific type of product"""
  def __init__(self, name:str, price:float, quantity:int, active:bool=True):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.active = active


    # self.name exceptions
    # is name a str?
    if not isinstance(self.name, str):
      raise TypeError("Error: Name must be a string!")

    # is name empty?
    if len(self.name) == 0:
      raise ValueError("Error: Name must be an empty string")


    # self.price exceptions

    # is price a float?
    if isinstance(self.price, int):
      self.price = float(self.price)
    elif not isinstance(self.price, float):
      raise ValueError("Error: Price must be a float number!")

    # is price negative?
    if self.price < 0:
      raise ValueError("Error: Price must not be negative!")


    # self.quantity exceptions
    self._validade_quanity()

  def _validade_quanity(self):
    # is quantity an int=
    if not isinstance(self.quantity, int):
      raise ValueError("Error: Quantity must be an integer!")

    # is quantity negative?
    if self.quantity < 0:
      raise ValueError("Error: Quantity must not be negative")


  # hier eibauen, dass man nur quantity bentutzen muss
  # 1. self.quanitity() = x
  # 2. print(self.quantitiy())

  def get_quantity(self) -> int:
    """returns the quantity of the Product instance"""
    return self.quantity

  def set_quantity(self, quantity):
    """sets the quantity of the Product intace. If self.quanity == 0, the product is deactivated"""
    self.quantity = quantity
    if self.quantity == 0:
      self.active = False


  def is_active(self):
    """shows, if the instace is active or not"""
    return self.active


  def activate(self):
    """activates the instace"""
    self.active = True


  def deactivate(self):
    """deactivates the instace"""
    self.active = False


  def show(self):
    """shows the instace-variable values of name, price and quanity"""
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


  def buy(self, quantity):
    """executes a 'buy' action for the product. checks if given quanity is valid calculates new quanity of the product"""
    total_price = self.price * quantity

    if self.quantity < quantity:
      # raise will be risen by store.py:38
      raise ValueError(f"Not enough {self.name}´s in stock. Only {self.quantity} {self.name}´s left.")
    else:
      self.quantity -= quantity

    if self.quantity == 0:
      self.active = False
      return f"Total Price: {total_price}, new product quantiy: {self.quantity}"


class DigitalProduct(Product):
  def __init__(self, name, price):
    super().__init__(name, price, quantity=0)
    self.quantity = inf


    # self.quantity exceptions
    self._validade_quanity()


  def _validade_quanity(self):
    """if self.quantity is not 'inf' ValueError will be raised"""
    if self.quantity != inf:
      raise ValueError("Quantity for digital products must always be 'inf'")

  def set_quantity(self, quantity):
    """self.quanity must not be changed"""
    raise AttributeError("Quantity for digital products must always be 'inf'")



class LimitedProduct(Product):
  def __init__(self, name, price, quantity, maximum):
    super().__init__(name, price, quantity)
    self.maximum = maximum


  @property
  def maximum(self):
    return self.maximum


  @maximum.setter
  def maximum(self, new_maximum):
    if new_maximum < 0:
      raise ValueError("Purchuasion must not be negative!")
    else:
      self.maximum = new_maximum


  def buy(self, quantity):
    """executes a 'buy' action for the product. checks if given quanity is valid calculates new quanity of the product"""
    super().buy(quantity)
    if quantity > self.maximum:
      raise(f"{str(self).upper} can only purchuated {self.maximum} times!")



  # LimitedProduct weiter ausformulieren
  # purchased x times coden












