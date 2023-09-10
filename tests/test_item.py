"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os.path

from src import item

os.path.join('src/items.csv', 'tests/test_file.scv')


def test_item_init(item1):
    isinstance(item1.name, str)
    isinstance(item1.price, float)
    isinstance(item1.quantity, int)

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 60000

def test_apply_discount(item1):
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 10000

def test_string_to_number(item1):
    assert item1.string_to_number("6") == 6
    assert item1.string_to_number(6.0) == 6
