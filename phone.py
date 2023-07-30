from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)


phone1 = Item("jscPhonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Item("jscPhonev20", 700, 5)
phone2.broken_phones = 1
