import pytest

from src.item import Item

@pytest.fixture
def item1():
    item1 = Item('Планшет', 20000, 3)
    return item1
