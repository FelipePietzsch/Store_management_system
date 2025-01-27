from abc import ABC

class Promotion(ABC):
  def __init__(self, promotion):
    self.promotion = promotion


  @property
  def promotion(self):
    return self.promotion


  @promotion.setter
  def promotion(self, new_promotion):
    self.promotion = new_promotion
