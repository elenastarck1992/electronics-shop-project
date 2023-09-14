import csv
import os.path

filename = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join(filename)

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        Item.all.append(self)
        self.__name = name[:10]
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open(cls.CSV_PATH, newline='', encoding='cp1251') as f:
            data = csv.DictReader(f)
            for row in data:
                price_int = cls.string_to_number(row['price'])
                quantity_int = cls.string_to_number(row['quantity'])
                cls(row['name'], price_int, quantity_int)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
