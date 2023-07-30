# When to use class and static methods

class Item:
    # use static method when we want to do something that should not be unique per instance
    # Has relationships with the class but does not interact with any class-specific data
    @staticmethod
    def is_integer(num):
        pass

    # Has a relationship with the class but used to manipulate different structures of data to instantiated objects
    # Does not need to create an object
    # Asking the class to do something specific
    @classmethod
    def instantiate_from_something(cls):
        pass

