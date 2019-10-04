from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare Items
item = {
    'sword':  Item("sword",
                     "The ancient sword of Excalibur"),

    'gun':  Item("Gun",
                         "357 Magnum, 6 Shots"),
    'club':  Item("Club",
                         "Louisville Slugger, 36 inches long"),
}

sword = item["sword"].name
gun = item["gun"].name
club = item["club"].name


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']


outside.add_item(gun)
foyer.add_item('gun')
overlook.add_item('club')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

bob = Player("Bob", room['outside'])
current_room = bob.current_room
current_desc = bob.current_room.description
room_items = current_room.items
directions = ["n", "s", "e", "w"]
value = False


print(f"You are currently in {current_room}. This is where {current_desc}. Located here is: {room_items}")
print(room_items)
while value is not True:
        command = input("Enter a command (n, s, e, w, or q to quit the game)")
        if command == "q":
            print(f"Goodbye {bob.name}")
            value = False
        if command not in directions:
            print("you must choose a valid command!!")
            command = input("Enter a command (n, s, e, w, or q to quit the game)")
        if command in directions:
            move = f"{command}_to"
            if hasattr(current_room, move):
                current_room = getattr(current_room, move)
                room_name = current_room.name
                outside.remove_item(gun)
                print("sword is dead", room_items)
                print("now the room is:", current_room)
            else:
                print(f"There is no room in that direction")
                command = input("Enter a command (n, s, e, w, or q to quit the game)")

