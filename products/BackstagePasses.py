from abc import ABC

from utils.Product import Product


class BackstagePasses(Product, ABC):
    """
    Backstage passes class
    """

    SELL_IN_FIRST_THRESHOLD = 10
    SELL_IN_FIRST_THRESHOLD_INCREASE = 1

    SELL_IN_SECOND_THRESHOLD = 5
    SELL_IN_SECOND_THRESHOLD_INCREASE = 2

    SELL_IN_THIRD_THRESHOLD_INCREASE = 3

    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update_quality(self):
        """
        Updates Backstage passes quality
        """
        if self.sell_in > self.SELL_IN_FIRST_THRESHOLD:
            self.item.quality += self.SELL_IN_FIRST_THRESHOLD_INCREASE
        elif self.sell_in > self.SELL_IN_SECOND_THRESHOLD:
            self.item.quality += self.SELL_IN_SECOND_THRESHOLD_INCREASE
        else:
            self.item.quality += self.SELL_IN_THIRD_THRESHOLD_INCREASE
