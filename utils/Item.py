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
