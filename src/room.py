# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"Room: {self.name} is {self.description}"
    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"

    def add_item(self, item):
        """Adds an item to self.items list"""
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)