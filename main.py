from programm_modules.product import Product, NonStockedProduct, LimitedProduct
from programm_modules.store import Store
from programm_modules.menu import User_Interface
from math import inf
from programm_modules.promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree


def main():
    """Contais all products, initialiates the instance 'best_buy' from the Store class and starts the best_buy 'shop'"""
    twenty_percent_promotion = PercentDiscount("20% off!!!", 20)
    second_half_price =SecondHalfPrice("Second half price!!!")
    third_one_free = ThirdOneFree("Third_one_free!!!")

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Microsoft_word_software", price=500),
        LimitedProduct("Shipping_fee", price=50, quantity=inf, maximum=1),
        NonStockedProduct("Microsoft 8 Licence", 300, promotion=twenty_percent_promotion),
        Product("Galaxy fold S", price=1200, quantity=230, promotion=second_half_price),
        Product("ReMarkable_2", price=250, quantity=1000, promotion=third_one_free)
        ]
    best_buy = Store(product_list)

    user_interface = User_Interface(best_buy)

    user_interface.run()


if __name__ == "__main__":
    main()


