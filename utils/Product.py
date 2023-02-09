import abc
from abc import ABC

from gilded_rose import Item


class Product(ABC):
    """
    Product class

    Attributes:
        item (Item): Item object
    """

    def __init__(self, name, sell_in, quality):
        self.item = Item(name, sell_in, quality if quality < 50 else 50)

    @property
    def name(self):
        """
        Returns the name of the product
        """
        return self.item.name

    @property
    def sell_in(self):
        """
        Returns the sell in date of the product
        """
        return self.item.sell_in

    @property
    def quality(self):
        """
        Returns the quality of the product
        """
        return self.item.quality

    def update_quality(self):
        """
        Updates a product
        """
        decrease_value = 1

        if self.sell_in <= 0:
            decrease_value = 2

        self.item.quality -= decrease_value

        if self.item.quality < 0:
            self.item.quality = 0

        if self.item.quality > 50:
            self.item.quality = 50

    def update_sell_in(self):
        """
        Updates the sell in date
        """
        self.item.sell_in -= 1

    def update(self):
        """
        Updates a product
        """
        self.update_sell_in()
        self.update_quality()

    def __str__(self):
        return self.item.__str__()
