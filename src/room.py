# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Room: {self.name} is {self.description}"
    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.description)})"


outs = Room("outside", "this is out of the house")

print(repr(outs))