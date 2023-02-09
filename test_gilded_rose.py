# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    """
    This is a test class for the Gilded Rose Kata
    """

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_quality_never_over_50(self):
        """
        Test that quality is never over 50
        """
        items = [Item("test_product", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)




if __name__ == '__main__':
    unittest.main()
