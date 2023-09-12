"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os.path
from src.item import Item

filename = '../tests/test_file.csv'
path = os.path.join(filename)


def test_item_init(item1):
    assert isinstance(item1.name, str)
    assert isinstance(item1.price, int)
    assert isinstance(item1.quantity, int)

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 60000

def test_apply_discount(item1):
    item1.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 10000

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_name(item1):
    assert item1.name == 'Планшет'
    item1.name = 'Микроволновка'
    assert item1.name == 'Микроволно'

def test_string_to_number(item1):
    assert item1.string_to_number("6") == 6
    assert item1.string_to_number(6.0) == 6
