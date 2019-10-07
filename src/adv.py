
import os
from room import Room
from player import Player
from item import Item


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """
                Dim light filters in from the south.
                Dusty passages run north and east."""
                                 ),
    
    'overlook': Room("Grand Overlook", """
                A steep cliff appears before you, falling into the darkness. 
                Ahead to the north, a light flickers in the distance, 
                but there is no way across the chasm."""
                                        ),

    'narrow':   Room("Narrow Passage", """
                The narrow passage bends here from west to north.
                he smell of gold permeates the air."""
                ),

    'treasure': Room("Treasure Chamber", """
                You've found the long-lost treasure chamber! 
                Sadly, it has already been completely emptied by earlier adventurers. 
                The only exit is to the south."""
                ),
}


# # Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# all the items
item = {
    "sword" : Item("sword", "This sword will pretect you!"),
    "greenapple" : Item(" green apple", "This green apple will give you life"),
    "redapple" : Item(" red apple", "This green apple will give more life"),
    "shield" : Item("shield", "This shield will pretect you"),
    "water" : Item("water", "This water will give you extra life"),
    "rope" : Item("rope", "This rope will alow you to climb or decend"),
    "map" : Item("map", "This map will guide you"),
    "cross" : Item("cross", "This cross will give you extra pretection"),
    "fire" : Item("fire", "This fire will pretect you against the dark"),
}



def drop_items_in_room():
    room['outside'].items =  [item['sword']]
    room['foyer'].items = [item['redapple'], item['shield']]
    room['overlook'].items =  [item['shield'], item['greenapple']]
    room['narrow'].items = [item['sword'], item['rope'], item['cross']]
    room['treasure'].items = [item['water'], item['map'], item['fire']]


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


def get_user_input(output_str):
    try:
        user_input = input(output_str + " \n> ")
        return user_input.lower()
    except TypeError:
        return ""


# get valid direction from the room
def get_valid_directions(room):
    valid_directions = ""

    if room.n_to != None:
        valid_directions +=  "n: north "

    if room.s_to != None:
        valid_directions +=  "s: south "

    if room.e_to != None:
        valid_directions +=  "e: east "

    if room.w_to != None:
        valid_directions +=  "w: west "

    return valid_directions + "\np: pick item\nq: quit"

# create a string from available rooms
def create_room_dir_str(room):
    valid_directions = ""

    if room.n_to != None:
        valid_directions +=  "n"

    if room.s_to != None:
        valid_directions +=  "s"

    if room.e_to != None:
        valid_directions +=  "e"

    if room.w_to != None:
        valid_directions +=  "w"

    return valid_directions + "qp"


# get valid path directions from valid_direction string
def get_path(valid_directions):
    for c in valid_directions:
        print(c)

def move_to_current_room(player, user_input):
    if user_input == 'n': 
        player.current_room =  player.current_room.n_to 
    elif user_input == 's': 
        player.current_room =  player.current_room.s_to
    elif user_input == 'w': 
        player.current_room =  player.current_room.w_to
    elif user_input == 'e': 
        player.current_room =  player.current_room.e_to    

def pick_item():
    return int(get_user_input("Pick 1 Item:"))
 
  


def adv_game():
    os.system("clear")
    drop_items_in_room()
    player_name = get_user_input("Player name: ")
    player = Player(player_name, room['outside'])

    while True:
        current_room = player.current_room
        print(current_room,"\n" ,current_room.get_room_items(),"\n" * 2)
        print(player.get_player_items())
        
        
        user_input = get_user_input(get_valid_directions(current_room))
        print(current_room, "\n" * 3)
        
        
       

        # rooms_key_str = create_room_dir_str(current_room)
        # print(rooms_key_str)
        # if rooms_key_str.find(user_input) == -1:
        #     print("Error, please try again")
        #     continue
        if user_input == 'q':
            print("Thank you for playing!")
            break
        elif user_input == 'p':
            i = pick_item()
            item = current_room.items[i]
            player.items.append(item)
            current_room.items.remove(item)
            print(player.name + " picked up\n" + item)
        else:
            move_to_current_room(player, user_input)

        os.system("clear")


if __name__ == '__main__':
    adv_game()



