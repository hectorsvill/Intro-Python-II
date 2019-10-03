# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room
# from item import Item

class Player:
    def __init__(self,name, room):
        super().__init__()
        self.name = name
        self.current_room = room
        self.items = []


