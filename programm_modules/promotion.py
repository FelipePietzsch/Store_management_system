from abc import ABC, abstractmethod


class Promotion(ABC):
	"""Abstract base class for all promotion types."""
	def __init__(self, promotion_type:str):
		if not isinstance(promotion_type, str) or promotion_type == "":
			raise ValueError("promotion_type must be a non-empty string.")
		
		self.promotion_type = promotion_type


	@abstractmethod
	def apply_promotion(self, product, quantity):
		"""Abstract method; returns the price, after promotion"""
		pass



class PercentDiscount(Promotion):
	"""Represents a percentage discount promotion."""
	def __init__(self, promotion_type, percent_value:int):
		super().__init__(promotion_type)
		if not isinstance(percent_value, int):
			raise TypeError("Percent must be an integer!")
		if not 0 < percent_value <= 100:
			raise ValueError("Percent must be higher than 0 and lower/equal 100 (inclusive)!")
		
		# sets percent_value and calculates factor for multiplication
		self.percent_value = percent_value / 100.0

	def apply_promotion(self, product, quantity: int):
		"""Applies the percentage discount to the product's price."""
		try:
			if quantity <= 0:
				raise ValueError("Qantity must be a positive, to apply a promotion")
			
			original_price = product.price * quantity
			promotion_price = original_price * (1 - self.percent_value)
			return promotion_price
		
		# if the product has no price attribute
		except AttributeError:
			raise TypeError("Product object does not have a 'price' attribute.")
		# Catch any other unexpected errors
		except Exception as e:
			print(f"An unexpected error occurred in PercentDiscount.apply_promotion: {e}")
			return product.price * quantity  # Fallback to original price

class SecondHalfPrice(Promotion):
	"""Represents a 'second item half price' promotion."""
	def apply_promotion(self, product, quantity):
		"""Second items costs the half price"""
		try:
			if quantity <= 0:
				raise ValueError("Quantity must be positive to apply promotion.")
			
			if not hasattr(product, 'price') or not isinstance(product.price, (int, float)):
				raise TypeError("Product must have a numeric 'price' attribute.")
			
			half_price_products = quantity // 2
			full_price_products = quantity - half_price_products
	
			half_price = half_price_products * product.price / 2
			full_price = full_price_products * product.price
	
			promotion_price = half_price + full_price
	
			return promotion_price
		
		except TypeError as te:
			print(f"Error in SecondHalfPrice promotion: {te}")
		except Exception as e:
			print(f"An unexpected error occurred in SecondHalfPrice.apply_promotion: {e}")
			return product.price * quantity # Fallback to original price


class ThirdOneFree(Promotion):
	"""Represents a 'buy two, get one free' (or every third item free) promotion."""
	def apply_promotion(self, product, quantity):
		"""    Applies the 'every third item is free' promotion"""
		try:
			if quantity <= 0:
				raise ValueError("Quantity must be positive to apply promotion.")
			
			if not hasattr(product, 'price') or not isinstance(product.price, (int, float)):
				raise TypeError("Product must have a numeric 'price' attribute.")
		
			third_products = quantity // 3
			full_price_products = quantity - third_products
	
			promotion_price = full_price_products * product.price
	
			return promotion_price
		
		except TypeError as te:
			print(f"Error in ThirdOneFree promotion: {te}")
		except Exception as e:
			print(f"An unexpected error occurred in ThirdOneFree.apply_promotion: {e}")
			return product.price * quantity # Fallback to original price