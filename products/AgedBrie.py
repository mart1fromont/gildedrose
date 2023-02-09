from abc import ABC

from utils.Product import Product


class AgedBrie(Product, ABC):
    """
    Aged Brie class
    """

    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        """
        Updates Aged Brie quality
        """
        self.item.quality += 1
