# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from gilded_rose import *
from products.AgedBrie import AgedBrie
from products.BackstagePasses import BackstagePasses
from products.Conjured import Conjured
from products.Sulfuras import Sulfuras
from utils.Item import Item
from utils.Product import Product

# Constants
DEFAULT_NUMBER_OF_DAYS = 2

if __name__ == "__main__":
    items = [
        Product(name="+5 Dexterity Vest", sell_in=10, quality=20),
        AgedBrie(sell_in=2, quality=0),
        Product(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Sulfuras(sell_in=0),
        Sulfuras(sell_in=-1),
        BackstagePasses(sell_in=15, quality=20),
        BackstagePasses(sell_in=10, quality=49),
        BackstagePasses(sell_in=5, quality=49),
        Conjured(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    # If we have a number of days as argument, use it
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    else:
        days = DEFAULT_NUMBER_OF_DAYS

    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")

        for item in items:
            print(item)

        print("")
        GildedRose(items).update_quality()
