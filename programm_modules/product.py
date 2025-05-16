from math import inf
from programm_modules.promotion import Promotion

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
		self.product_quantity = quantity
		self.active = active
		self.product_promotion = promotion_class
		
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
		if self.product_promotion:
			
			if not isinstance(self.product_promotion, Promotion):
				raise ValueError("Error: Promotion must be a Promotion-class")

		# self.product_quantity exceptions
		self._validade_quanity()
	
	def _validade_quanity(self):
		# is product_quantity an int or a flaot
		if not isinstance(self.product_quantity, int) and not isinstance(self.product_quantity, float):
			raise ValueError("Error: product_quantity must be an integer!")
		
		# is quantity negative?
		if self.product_quantity < 0:
			raise ValueError("Error: product_quantity must not be negative")
	
	@property
	def quantity(self):
		"""returns quantity"""
		return self.product_quantity
	
	@quantity.setter
	def quantity(self, value):
		"""
		Sets the product_quantity of the product.
		Deactivates the product if product_quantity becomes 0.
		"""
		if not isinstance(value, int) and not isinstance(value, float):
			raise ValueError("product_quantity must be an integer or float!")
		
		if value < 0:
			raise ValueError("product_quantity must not be negative!")
		
		self.product_quantity = value
		
		if self.product_quantity == 0:
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
		"""shows the product-variable values of name, price and product_quantity"""
		if isinstance(self.product_promotion, Promotion):
			return f"{self.name}, Price: {self.price}, Quantity: {self.product_quantity}, Promotion: {self.product_promotion}"
		
		return f"{self.name}, Price: {self.price}, Quantity: {self.product_quantity}"
	
	def buy(self, product_quantity) -> float:
		"""
		Executes a 'buy' action for the product.
		Checks if the given product_quantity is valid and calculates the new product_quantity of the product.
		
		Args:
		quantity_to_buy (int): The amount of the product to buy.
		
		Returns:
		float: The total price for the purchased product_quantity.
		
		Raises:
		ValueError: If there is not enough stock, or if the product_quantity is not positive.
		"""
		total_price = self.price * product_quantity
		
		# reduces price by promotion
		# if self._promotion isinstance from Poromtion class
		if isinstance(self.product_promotion, Promotion):
			total_price = self.product_promotion.apply_promotion(self, product_quantity)
		
		if self.product_quantity < product_quantity:
			# exception will be risen by store.py:38
			raise ValueError(f"Not enough {self.name}´s in stock. Only {self.product_quantity} {self.name}´s left.")
		else:
			self.product_quantity -= product_quantity
		
		if self.product_quantity == 0:
			self.active = False
		# f"Total Price: {total_price}, new product quantiy: {self.product_quantity}"
		
		return total_price
	
	@property
	def promotion(self):
		"""Gets the promotion applied to the product."""
		return self.product_promotion
	
	@promotion.setter
	def promotion(self, new_promotion):
		"""sets the promotion for the product"""
		if isinstance(new_promotion, Promotion):
			self.product_promotion = new_promotion
		
		else:
			raise TypeError("promotion must be a instance of the Promotion class")


class NonStockedProduct(Product):
	"""Represents a product that is not stocked physically (e.g., software) and has infinite product_quantity."""
	def __init__(self, name, price, product_quantity=inf, active=True, promotion_class=None, ):
		super().__init__(name, price, product_quantity, active, promotion_class)
		
		# self.product_quantity exceptions
		self._validade_quanity()
	
	def _validade_quanity(self):
		"""If self.product_quantity is not 'inf' ValueError will be raised"""
		if not isinstance(self.product_quantity, float):
			raise ValueError("product_quantity for digital products must always be 'inf'")
	
	def set_quantity(self, product_quantity):
		"""self.quanity must not be changed"""
		raise AttributeError("product_quantity for digital products must always be 'inf'")


class LimitedProduct(Product):
	def __init__(self, name, price, product_quantity, maximum, active=True, promotion_class=None):
		super().__init__(name, price, product_quantity, active, promotion_class)
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
	
	def buy(self, product_quantity):
		"""Executes a 'buy' action for the limited product.
        Checks if the purchase product_quantity exceeds the maximum limit."""
		super().buy(product_quantity)
		if product_quantity > self._maximum:
			raise ValueError(
				f"{str(self).upper()} can only purchuated {self._maximum} times!")  # Corrected to ValueError and improved message


