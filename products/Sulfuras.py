from abc import ABC

from utils.Product import Product


class Sulfuras(Product, ABC):
    """
    Sulfuras class
    """

    SULFURAS_QUALITY = 80

    def __init__(self, sell_in):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, self.SULFURAS_QUALITY)
        self.item.quality = self.SULFURAS_QUALITY

    def update_quality(self):
        """
        Updates Sulfuras quality
        """
        pass

    def update_sell_in(self):
        """
        Updates Sulfuras sell in date
        """
        pass
