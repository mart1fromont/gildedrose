# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """
    This is a test class for the Gilded Rose Kata
    """

    def test_quality_cannot_be_negative(self):
        """
        Test that quality cannot be negative
        """
        items = [Item("test_product", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_never_over_50(self):
        """
        Test that quality is never over 50
        """
        items = [Item("test_product", 0, 60)]
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_never_changes(self):
        """
        Test that Sulfuras quality never changes
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_backstage_passes_product(self):
        """
        Test that backstage passes quality increases by 2 when sell_in is 10 or less, and by 3 when sell_in is 5 or less
        Also check that quality is 0 when sell_in is 0
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
