import pytest
from programm_modules.product import Product, NonStockedProduct, LimitedProduct
from programm_modules.promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree
from programm_modules.store import Store

# 1. Test: Produkt erstellen und kaufen
def test_product_creation_and_purchase():
  product = Product("Banana", 1.0, 10)

  assert product.name == "Banana"
  assert product.price == 1.0
  assert product.quantity == 10

  total_price = product.buy(3)
  assert total_price == f"{total_price}"
  assert product.quantity == 7  # 10 - 3

  with pytest.raises(ValueError):
    product.buy(8)  # Mehr kaufen, als vorhanden


# 2. Test: PercentDiscount Promotion
def test_percent_discount():
  product = Product("Apple", 2.0, 10)
  discount = PercentDiscount("10% off", 10)
  product.promotion(discount)

  total_price = product.buy(5)
  assert total_price == 'Total Price: 9.0, new product quantiy: 5'  # 5 * 2.0 = 10, 10 - 10% = 9.0


# 3. Test: SecondHalfPrice Promotion
def test_second_half_price():
  product = Product("Orange", 3.0, 10)
  promotion = SecondHalfPrice("Buy 1 get 2nd half off")
  product.promotion(promotion)

  total_price = product.buy(4)
  # 2 volle Preise: 2 * 3 = 6
  # 2 halbe Preise: 2 * 1.5 = 3
  assert total_price == 9


# 4. Test: ThirdOneFree Promotion
def test_third_one_free():
  product = Product("Mango", 4.0, 9)
  promotion = ThirdOneFree("Buy 2 get 1 free")
  product.promotion(promotion)

  total_price = product.buy(6)
  # 2 Mangos kostenlos, 4 bezahlt: 4 * 4 = 16
  assert total_price == 16


# 5. Test: Bestellung im Store
def test_store_order():
  banana = Product("Banana", 1.0, 10)
  apple = Product("Apple", 2.0, 5)

  product_list = [banana,
                  apple]

  store = Store(product_list)


  order_list = [(banana, 3), (apple, 2)]
  total_price = store.order(order_list)

  assert total_price == (3 * 1.0) + (2 * 2.0)  # 3 + 4 = 7
  assert banana.quantity == 7
  assert apple.quantity == 3


# 6. Test: Bestellung mit Versand
def test_order_with_shipping():

  book = Product("Book", 10.0, 5)
  shipping = NonStockedProduct("Shipping", 5.0)  # Versand als Produkt

  product_list = [book,
                  shipping]

  store = Store(product_list)

  order_list = [(book, 1), (shipping, 1)]
  total_price = store.order(order_list)

  assert total_price == 15.0  # 10 (Buch) + 5 (Versand)


