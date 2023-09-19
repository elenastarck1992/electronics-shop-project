from src.item import Item


class KeyBoardMixin:
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'

        else:
            self.__language = 'EN'


class Keyboard(KeyBoardMixin, Item):

    def __init__(self, name: str, price: int, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language
