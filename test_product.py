from tkinter import XView

import main
import pytest
import math
from programm_modules.product import Product
from programm_modules.menu import User_Interface
from programm_modules.store import Store


def test_negative_priced_object():
  with pytest.raises(ValueError):
    iphone = Product("iPone X", -1.5, 1000)
    iphone = Product("iPhone X", "test", 2)

def test_negative_quantitated_objekt():
  with pytest.raises(ValueError):
    iphone = Product("iPhone X", 150.8, -10)
    ipohne = Product("iPhone X", 5, "test")

def test_different_name_inputs():
  with pytest.raises(TypeError):
    iphone = Product(["iPhone", "X"], 2, 1000)
    iphone = Product(22, 2, 1000)

def test_empty_name_input():
  with pytest.raises(ValueError):
    iphone = Product("", 2, 100)

def test_when_quantity_zero_active_is_False():
  iphone = Product("iPhone X", 1, 1)
  assert iphone.get_quantity() == 1
  assert iphone.is_active() == True
  iphone.buy(1)
  assert iphone.get_quantity() != 1
  assert iphone.get_quantity() == 0
  assert iphone.is_active() == False
  assert iphone.is_active() != True

def test_buy_more_than_is_in_stock():
  with pytest.raises(ValueError):
    iphone = Product("iPhone", 1, 1)
    iphone.buy(2)


test_negative_quantitated_objekt()
test_negative_priced_object()
test_different_name_inputs()