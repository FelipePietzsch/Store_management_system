"""
This program simulates a simple command-line store application.
It allows users to list products, place orders, and see the total
number of items in the store. The program features different product
types (standard, non-stocked, limited) and various promotion types
(percentage discount, second item half price, third item free).
"""
from programm_modules.product import Product, NonStockedProduct, LimitedProduct
from programm_modules.store import Store
from programm_modules.menu import User_Interface
from math import inf
from programm_modules.promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree


def main():
	"""
	Contains all products, initializes the 'best_buy' instance
	from the Store class, and starts the 'best_buy' shop UI.
	"""
	try:
		# Initialize promotions
		twenty_percent_promotion = PercentDiscount("20% off!!!", 20)
		second_half_price = SecondHalfPrice("Second half price!!!")
		third_one_free = ThirdOneFree("Third_one_free!!!")
	
		# Initialize product list
		product_list = [
			Product("MacBook Air M2", price=1450, quantity=100),
			Product("Bose QuietComfort Earbuds", price=250, quantity=500),
			Product("Google Pixel 7", price=500, quantity=250),
			NonStockedProduct("Microsoft_word_software", price=500),
			LimitedProduct("Shipping_fee", price=50, quantity=inf, maximum=1), # Assuming inf quantity for a service like shipping is intentional
			NonStockedProduct("Microsoft 8 Licence", 300, Promotion=twenty_percent_promotion),
			Product("Galaxy fold S", price=1200, quantity=230, Promotion=second_half_price),
			Product("ReMarkable_2", price=250, quantity=1000, Promotion=third_one_free)
		]
		best_buy = Store(product_list)
	
		user_interface = User_Interface(best_buy)
	
		user_interface.run()
	
	except ValueError as ve:
		print(f"Error during initialization: {ve}")
	except TypeError as te:
		print(f"Error during initialization: {te}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	
	
	if __name__ == "__main__":
		main()