from programm_modules.product import Product, NonStockedProduct, LimitedProduct  # Import specific classes
import math
class Store:
	"""Contains all data and functions to interact with a store object."""
	
	def __init__(self, products: list):
		"""Initializes a new Store"""
		if not isinstance(products, list):
			raise TypeError("Initial products must be provided as a list.")
		
		for product in products:
			# Check if items are instances of Product
			if not isinstance(product, Product):
				raise TypeError("All items in the initial product list must be Product instances.")
		
		self.products = products
	
	def add_product(self, product_to_add: Product):
		"""Adds a new product to the store."""
		if not isinstance(product_to_add, Product):
			raise TypeError("Only Product instances can be added to the store.")
		
		self.products.append(product_to_add)
		
		print(f"Product '{product_to_add.name}' added to the store.")
	
	def remove_product(self, product_to_remove: Product):
		"""
		Removes a product from the store.
		Note: The product will be removed, not just deactivated.

		Args:
			product_to_remove (Product): The Product instance to remove.

		Raises:
			TypeError: If product_to_remove is not a Product instance.
			ValueError: If the product is not found in the store.
		"""
		if not isinstance(product_to_remove, Product):
			raise TypeError("Only Product instances can be removed from the store.")
		
		try:
			self.products.remove(product_to_remove)
			print(f"Product '{product_to_remove.name}' removed from the store.")
		
		except ValueError:
			# This occurs if product_to_remove is not in self.products
			raise ValueError(f"Product '{product_to_remove.name}' not found in the store.")
	
	def get_total_quantity(self) -> int:
		"""
		Returns the total amount of all items in the store.
		
		For Products where product.product_qantity is inf, it counts each type as 1 if present,
		as their quantity is conceptually infinite.
		"""
		total_quantity = 0
		for product_item in self.products:
			
			try:
				
				# check if product_item hasattr: quantity and is an int or float
				if hasattr(product_item, 'product_quantity') and isinstance(product_item.product_quantity, (int, float)) and product_item.is_active():
					
					# Some Products, like NonStockedProducts have 'inf' quantity, so it counts as 1 unique item type if active.
					if math.isinf(product_item.product_quantity):
						total_quantity += 1
					
					else:
						# Ensure it's an int for summing
						total_quantity += int(product_item.product_quantity)
			
			except AttributeError:
				print(f"Warning: Item {product_item} in store does not have a 'quantity' or 'is_active' attribute.")
			
			except TypeError:
				print(f"Warning: Quantity for item {product_item.name} is not a number.")
		
		return total_quantity
	
	def get_all_products(self) -> list:
		"""Returns a list of all active products in the store."""
		active_products = []
		
		for product_item in self.products:
			
			try:
				if product_item.is_active():
					active_products.append(product_item)
			
			except AttributeError:
				print(f"Warning: Item {product_item} in store does not have the 'is_active' attribute.")
		
		return active_products
	
	def order(self, order_list: list) -> float:
		"""
		Processes a list of ordered items.
		Each item in order_list should be a tuple: (Product instance, quantity).
		Executes the '.buy()' method for each product in the order.

		Args:
			order_list (list): A list of tuples, where each tuple contains
							   a Product instance and the desired quantity.

		Returns:
			float: The total price of the order.
		"""
		total_price = 0.0  # Initialize as float
		
		if not isinstance(order_list, list):
			print("Error: Order must be a list.")
			
			return 0.0
		
		for item_tuple in order_list:
			
			try:
				if not (isinstance(item_tuple, tuple) and len(item_tuple) == 2):
					print(f"Warning: Invalid item format in order: {item_tuple}. Skipping.")
					continue
				
				product_obj, quantity = item_tuple
				
				if not isinstance(product_obj, Product):
					print(f"Warning: Invalid product object in order: {product_obj}. Skipping.")
					continue
				
				if not isinstance(quantity, int) or quantity <= 0:
					print(f"Warning: Invalid quantity for {product_obj.name}: {quantity}. Skipping.")
					continue
				
				# Check if the product is in this store's list of products and is active
				if product_obj not in self.products or not product_obj.is_active():
					print(
						f"Warning: Product '{product_obj.name}' is not available or not active in this store. Skipping.")
					continue
				
				# The buy method in Product class should handle stock and raise ValueError if not enough
				price_for_item = product_obj.buy(quantity)
				total_price += price_for_item
				print(f"Ordered {quantity} of {product_obj.name}. Subtotal: ${price_for_item:.2f}")
			
			except ValueError as ve:  # Catches errors from product.buy (e.g., insufficient stock, invalid quantity)
				print(f"Order Error for {getattr(product_obj, 'name', 'Unknown Product')}: {ve}")
			
			except TypeError as te:  # Catches type errors if product_obj is not as expected by buy()
				print(f"Order Processing Error for {getattr(product_obj, 'name', 'Unknown Product')}: {te}")
			
			except Exception as e:  # Catch any other unexpected errors during processing a single item
				print(
					f"An unexpected error occurred while processing item {getattr(product_obj, 'name', 'Unknown Product')} in order: {e}")
		
		return total_price
