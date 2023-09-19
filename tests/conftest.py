import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


class Thing:
    def __int__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

@pytest.fixture
def item1():
    item1 = Item('Планшет', 20000, 3)
    return item1

@pytest.fixture
def phone1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1

@pytest.fixture
def thing1():
    thing1 = Thing("Штуковина", 5000, 1)
    return thing1

@pytest.fixture
def kb1():
    kb1 = Keyboard('Dark Project KD87A', 9600, 5)
    return kb1
