from math import inf
from types import NoneType
from programm_modules.promotion import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree

class Product:
	"""
	Initializes a new Product.

	Args:
		name (str): The name of the product.
		price (float): The price of the product.
		quantity: The quantity of the product. Can be int or float (inf).
		active (bool, optional): Whether the product is active. Defaults to True.

	Raises:
		TypeError: If name is not a string or price is not a float/int or promotion_obj is not a Promotion instance.
		ValueError: If name is empty, price is negative, or quantity is negative.
	"""
	
	def __init__(self, name: str, price: float, quantity, active: bool = True, promotion_class:Promotion=None):
		self.name = name
		self.price = price
		self.quantity = quantity
		self.active = active
		self._product_promotion = promotion_class
		
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
		
		# if product promotion is None it is ignored
		if self._product_promotion:
			
			if isinstance(self._product_promotion, (Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree)):
				raise ValueError("Error: Promotion must be a Promotion-class")

		# self.quantity exceptions
		self._validade_quanity()
	
	def _validade_quanity(self):
		# is quantity an int or a flaot
		if not isinstance(self.quantity, int) and not isinstance(self.quantity, float):
			raise ValueError("Error: Quantity must be an integer!")
		
		# is quantity negative?
		if self.quantity < 0:
			raise ValueError("Error: Quantity must not be negative")
	
	@property
	def quantity(self):
		"""returns quantity"""
		return self._quantity
	
	@quantity.setter
	def quantity(self, value):
		"""
		Sets the quantity of the product.
		Deactivates the product if quantity becomes 0.
		"""
		if not isinstance(value, int) and not isinstance(value, float):
			raise ValueError("Quantity must be an integer or float!")
		
		if value < 0:
			raise ValueError("Quantity must not be negative!")
		
		self._quantity = value
		
		if self._quantity == 0:
			self.active = False
	
	def is_active(self):
		"""shows, if the product is active or not"""
		return self.active
	
	def activate(self):
		"""activates the product"""
		self.active = True
	
	def deactivate(self):
		"""deactivates the product"""
		self.active = False
	
	def show(self):
		"""shows the product-variable values of name, price and quantity"""
		if isinstance(self._product_promotion, Promotion):
			return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self._product_promotion}"
		
		return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
	
	def buy(self, quantity) -> float:
		"""
		Executes a 'buy' action for the product.
		Checks if the given quantity is valid and calculates the new quantity of the product.
		
		Args:
		quantity_to_buy (int): The amount of the product to buy.
		
		Returns:
		float: The total price for the purchased quantity.
		
		Raises:
		ValueError: If there is not enough stock, or if the quantity_to_buy is not positive.
		"""
		total_price = self.price * quantity
		
		# reduces price by promotion
		# if self._promotion isinstance from Poromtion class
		if isinstance(self._product_promotion, Promotion):
			total_price = self._product_promotion.apply_promotion(self, quantity)
		
		if self.quantity < quantity:
			# exception will be risen by store.py:38
			raise ValueError(f"Not enough {self.name}´s in stock. Only {self.quantity} {self.name}´s left.")
		else:
			self.quantity -= quantity
		
		if self.quantity == 0:
			self.active = False
		# f"Total Price: {total_price}, new product quantiy: {self.quantity}"
		
		return total_price
	
	@property
	def promotion(self):
		"""Gets the promotion applied to the product."""
		return self._product_promotion
	
	@promotion.setter
	def promotion(self, new_promotion):
		"""sets the promotion for the product"""
		if isinstance(new_promotion, Promotion):
			self._product_promotion = new_promotion
		
		else:
			raise TypeError("promotion must be a instance of the Promotion class")


class NonStockedProduct(Product):
	"""Represents a product that is not stocked physically (e.g., software) and has infinite quantity."""
	def __init__(self, name, price, quantity=inf, active=True, promotion_class=None, ):
		super().__init__(name, price, quantity, active, promotion_class)
		
		# self.quantity exceptions
		self._validade_quanity()
	
	def _validade_quanity(self):
		"""If self.quantity is not 'inf' ValueError will be raised"""
		if not isinstance(self.quantity, float):
			raise ValueError("Quantity for digital products must always be 'inf'")
	
	def set_quantity(self, quantity):
		"""self.quanity must not be changed"""
		raise AttributeError("Quantity for digital products must always be 'inf'")


class LimitedProduct(Product):
	def __init__(self, name, price, quantity, maximum, active=True, promotion_class=None):
		super().__init__(name, price, quantity, active, promotion_class)
		self._maximum = maximum
	
	@property
	def maximum(self):
		"""Gets the maximum purchase limit for this product."""
		return self._maximum
	
	@maximum.setter
	def maximum(self, new_maximum):
		"""Sets the maximum purchase limit for this product."""
		if new_maximum < 0:
			raise ValueError("Purchuasion must not be negative!")
		else:
			self._maximum = new_maximum
	
	def buy(self, quantity):
		"""Executes a 'buy' action for the limited product.
        Checks if the purchase quantity exceeds the maximum limit."""
		super().buy(quantity)
		if quantity > self._maximum:
			raise ValueError(
				f"{str(self).upper()} can only purchuated {self._maximum} times!")  # Corrected to ValueError and improved message


