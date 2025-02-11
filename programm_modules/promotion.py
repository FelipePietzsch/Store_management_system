from abc import ABC, abstractmethod


class Promotion(ABC):
  def __init__(self, promotion):
    self.promotion = promotion


  @abstractmethod
  def apply_promotion(self, product, quantity):
    """Abstract method; returns the price, after promotion"""
    pass



class PercentDiscount(Promotion):
  def __init__(self, promotion, percent:int):
    super().__init__(promotion)
    self.percent = percent
    self.validade_percent()


  def validade_percent(self):
    """Checks, if self.discount is initialated correct"""
    if not isinstance(self.percent, int):
      raise ValueError("Percent must be an integer!")

    if self.percent > 100:
      raise ValueError("Percent max is 100!")

    if self.percent < 0:
      raise ValueError("Percent must not be negative!")

    self.percent = self.percent * 0.01 # percent to float


  def apply_promotion(self, product, quantity):
    """Returns new price, after discount"""
    price = product.price * quantity
    promotion_price = price * (1 - self.percent)
    return promotion_price



class SecondHalfPrice(Promotion):
  def apply_promotion(self, product, quantity):
    """Second items costs the half price"""
    half_price_products = quantity // 2
    full_price_products = quantity - half_price_products

    half_price = half_price_products * product.price / 2
    full_price = full_price_products * product.price

    promotion_price = half_price + full_price

    return promotion_price



class ThirdOneFree(Promotion):
  def apply_promotion(self, product, quantity):
    """Evry third product is for free"""
    third_products = quantity // 3
    full_price_products = quantity - third_products

    promotion_price = full_price_products * product.price

    return promotion_price


