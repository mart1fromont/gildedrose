# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from products.AgedBrie import AgedBrie
from products.BackstagePasses import BackstagePasses
from products.Conjured import Conjured
from products.Sulfuras import Sulfuras
from utils.Product import Product


class GildedRoseTest(unittest.TestCase):
    """
    This is a test class for the Gilded Rose Kata
    """

    def test_brie(self):
        """
        Test that brie quality increases
        """
        items = [AgedBrie(sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    def test_peremption(self):
        """
        Test that quality decreases
        """
        items = [Product(name="Elixir of the Mongoose", sell_in=2, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(6, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual("Elixir of the Mongoose", items[0].name)
        self.assertEqual(4, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_quality_cannot_be_negative(self):
        """
        Test that quality cannot be negative
        """
        items = [Product("test_product", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_over_50(self):
        """
        Test that quality is never over 50
        """
        items = [Product("test_product", 0, 60)]
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_never_changes(self):
        """
        Test that Sulfuras quality never changes
        """
        items = [Sulfuras(0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_product(self):
        """
        Test that backstage passes quality increases by 2 when sell_in is 10 or less, and by 3 when sell_in is 5 or less
        Also check that quality is 0 when sell_in is 0
        """
        items = [BackstagePasses(10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

        items = [BackstagePasses(5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_conjured_product(self):
        """
        Test that conjured product quality decreases by 2
        """
        items = [Conjured("test_conjured_product", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)


if __name__ == '__main__':
    unittest.main()
