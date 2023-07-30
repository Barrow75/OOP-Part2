import csv


class Item:
    # class attributes - belongs to class itself, can be accessed through instance as well
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    # methods - 2 functions inside classes

    # Each instance we create this is called automatically
    # self = passes itself as the first argument when you call the methods.
    #   - Allows us to assign attributes from init methods to prevent us from assigning each instance we create
    def __init__(self, name, price, quantity):
        # Assign to self-object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property Decorator = Read Only Attribute
    @property
    def name(self):
        return self.__name

    # set a new value for that name
    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # decorators are used to modify or enhance the behavior of functions or methods
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'), price=float(item.get("price")), quantity=int(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        # count out floats that are point zero
        if isinstance(num, float):
            # count out floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @property
    def read_only_name(self):
        return "AAA"


print(Item.is_integer(7.5))
