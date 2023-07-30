# Object Orientated
# Creating an Instance = Creating an object

# Instantiate Instance - creating data that will represent something

from item import Item
from phone import Phone

item1 = Item("MyItem", 750, 2)
item1.name = "OtherItem"
#print(item1.read_only_name)
print(item1.name)
