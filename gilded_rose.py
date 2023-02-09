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
