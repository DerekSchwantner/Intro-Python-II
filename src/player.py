# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self):
        return f"Player: {self.name} is {self.current_room}"
    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"

derek = Player("John Smith", "outside")

print(derek)
print(repr(derek))