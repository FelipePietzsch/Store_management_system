import pytest
from programm_modules import product
from programm_modules import promotion
from programm_modules import store
from programm_modules import menu
from programm_modules.menu import User_Interface
from programm_modules.store import Store


def test_negative_priced_object():
  with pytest.raises(ValueError):
    iphone = product.Product("iPone X", -1.5, 1000)
    iphone = product.Product("iPhone X", "test", 2)

def test_negative_quantitated_objekt():
  with pytest.raises(ValueError):
    iphone = product.Product("iPhone X", 150.8, -10)
    ipohne = product.Product("iPhone X", 5, "test")

def test_different_name_inputs():
  with pytest.raises(TypeError):
    iphone = product.Product(["iPhone", "X"], 2, 1000)
    iphone = product.Product(22, 2, 1000)

def test_empty_name_input():
  with pytest.raises(ValueError):
    iphone = product.Product("", 2, 100)

def test_when_quantity_zero_active_is_False():
  iphone = product.Product("iPhone X", 1, 1)
  assert iphone.get_quantity() == 1
  assert iphone.is_active() == True
  iphone.buy(1)
  assert iphone.get_quantity() != 1
  assert iphone.get_quantity() == 0
  assert iphone.is_active() == False
  assert iphone.is_active() != True

def test_buy_more_than_is_in_stock():
  with pytest.raises(ValueError):
    iphone = product.Product("iPhone", 1, 1)
    iphone.buy(2)

# setup initial stock of inventory
product_list = [ product.Product("MacBook Air M2", price=1450, quantity=100),
                 product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 product.Product("Google Pixel 7", price=500, quantity=250),
                 product.NonStockedProduct("Windows License", price=125),
                 product.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotion.SecondHalfPrice("Second Half price!")
third_one_free = promotion.ThirdOneFree("Third One Free!")
thirty_percent = promotion.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price) # geht hier irgendwie zur falschen methode
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

test_negative_quantitated_objekt()
test_negative_priced_object()
test_different_name_inputs()

test_buy = Store(product_list)
user_menu = User_Interface(test_buy)

# buy tests for test_buy:
test_buy.get_all_products()
order_list = [(product_list[0], 5),
             (product_list[1], 100),
             (product_list[2], 50),
             (product_list[3], 50),
             (product_list[4], 1)
             ]
test_buy.order(order_list)



