
import os
from room import Room
from player import Player



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

user_input_description = "n: north | s: south | e: east | w: west | q: quit"





# get player name from user input
def get_player():
    user_input = ""
    try:
        user_input = input("player: name" + " \n> ")
    except TypeError:
        return -1
    return user_input


# give user valid directions and get user input 
def get_input(valid_directions):
    user_input = ""
    try:
        user_input = input(valid_directions + "\n> ")
    except TypeError:
        return -1
    return user_input


# get valid direction from the room
def get_valid_directions(room):
    valid_directions = ""

    if room.n_to != None:
        valid_directions +=  "n: north "

    if room.s_to != None:
        valid_directions +=  "s: south "

    if room.e_to != None:
        valid_directions +=  "e: east | "

    if room.w_to != None:
        valid_directions +=  "w: west | "

    return valid_directions + " \nq: quit"

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

    return valid_directions + "q"


# get valid path directions from valid_direction string
def get_path(valid_directions):
    for c in valid_directions:
        print(c)

def move_to_current_room(player, user_input):
    print(player.name, user_input)
    print(player.current_room)
    
    if user_input == 'n': 
        player.current_room =  player.current_room.n_to 
    elif user_input == 's': 
        player.current_room =  player.current_room.s_to
    elif user_input == 'w': 
        player.current_room =  player.current_room.w_to
    elif user_input == 'e': 
        player.current_room =  player.current_room.e_to    


def adv_game():
    os.system("clear")
    player_name = get_player()
    player = Player(player_name, room['outside'])

    while True:
        
        current_room = player.current_room
        valid_directions = get_valid_directions(current_room)
        print(current_room)
        user_input = get_input(valid_directions)
        
        if create_room_dir_str(current_room).find(user_input) == -1:
            print("Error, please try again")
            continue
        elif user_input == 'q':
            print("Thank you for playing!")
            break
        else:
            os.system("clear")
            move_to_current_room(player, user_input)




if __name__ == '__main__':
    adv_game()

