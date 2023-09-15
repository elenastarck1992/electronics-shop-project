import pytest

from src.item import Item
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
