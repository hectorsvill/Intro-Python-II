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
                                            The smell of gold permeates the air."""
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


def get_valid_directions(room):
    valid_directions = ""
    # print(room.n_to, room.s_to, room.e_to, room.w_to)
    if room.n_to != None:
        valid_directions +=  "n"

    if room.s_to != None:
        valid_directions +=  "s"

    if room.e_to != None:
        valid_directions +=  "e"

    if room.w_to != None:
        valid_directions +=  "w"
    return valid_directions

def get_input():
    user_input = ""
    try:
        user_input = input(user_input_description + " \n> ")
    except TypeError:
        return -1
    return user_input


def get_player():
    user_input = ""
    try:
        user_input = input("player: name"+ " \n> ")
    except TypeError:
        return -1
    
    
    return user_input
    

def adv_game():
    player_name = get_player()
    player = Player(player_name, room['outside'])

    print(player.current_room.name)
    print(get_valid_directions(player.current_room))
    # while True:
    #     user_input = get_input()
    #     if user_input == 'q':
    #         break
    #     elif "nsewq".find(user_input) == -1:
    #         print("Error, please try again")
    #         continue
    #     elif user_input == 'n': 
    #         print(user_input)
    #     elif user_input == 's':
    #         pass
    #     elif user_input == 'e':
    #         pass
    #     elif user_input == 'w':
    #         pass


if __name__ == '__main__':
    adv_game()

