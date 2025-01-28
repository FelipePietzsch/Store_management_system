from abc import ABC, abstractmethod


class Promotion(ABC):
  def __init__(self, product):
    self.product = product


  @abstractmethod
  def apply_promotion(self, quantity):
    """Abstract method; returns the price, after promotion"""
    pass



class PercentageDiscount(Promotion):
  def __init__(self, product, discount:int):
    super().__init__(product)
    self.discount = discount * 0.01 # percent to float
    self.validade_discount()


  def validade_discount(self):
    """Checks, if self.discount is initialated correct"""
    if not isinstance(self.discount, int):
      raise ValueError("Discount must be an integer!")

    if self.discount > 100:
      raise ValueError("Discount max is 100!")

    if self.discount < 0:
      raise ValueError("Discount must not be negative!")


  def apply_promotion(self, quantity):
    """Returns new price, after discount"""
    price = self.product.price * quantity
    promotion_price = price * self.discount
    return promotion_price



class SecondItemHalfPrice(Promotion):
  def apply_promotion(self, quantity):
    """Second items costs the half price"""
    half_price_products = quantity // 2
    full_price_products = quantity - half_price_products

    half_price = half_price_products * self.product.price / 2
    full_price = full_price_products * self.product.price

    promotion_price = half_price + full_price

    return promotion_price



class BuyTwoGetOneFree(Promotion):
  def apply_promotion(self, quantity):
    """Evry third product is for free"""
    third_products = quantity // 3
    full_price_products = quantity - third_products

    promotion_price = full_price_products * self.product.price

    return promotion_price




"""Ablauf:
Product bekommt eine variable(promotion), in die dann die Promotion classe kommt.
Die variable soll getter und setter bekommen.
Durch setter soll mann dann die Promotion class in die Product class bekommen.
Die 'buy' variable soll dann so umgestaltet werden, dass sie mit und ohne promotion funktioniert.
Wenn die variable 'promotion' - in der Product class - vorhanden ist, soll die promotion in der buy methode angewendet werden. 
"""