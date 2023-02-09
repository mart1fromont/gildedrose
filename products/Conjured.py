from abc import ABC

from utils.Product import Product


class Conjured(Product, ABC):
    """
    Conjured product class
    """

    CONJURED_DECREASE_VALUE = 2
    CONJURED_DECREASE_VALUE_AFTER_SELL_IN = 4

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        """
        Updates Conjured quality
        """
        if self.sell_in <= 0:
            self.item.quality -= self.CONJURED_DECREASE_VALUE_AFTER_SELL_IN
        else:
            self.item.quality -= self.CONJURED_DECREASE_VALUE
