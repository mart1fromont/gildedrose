# -*- coding: utf-8 -*-

class GildedRose(object):
    """
    This is a class for the Gilded Rose Kata

    Attributes:
        items (list): A list of products
    """

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    """
    Item class
    """

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality if self.name == "Sulfuras, Hand of Ragnaros" or quality < 50 else 50

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
