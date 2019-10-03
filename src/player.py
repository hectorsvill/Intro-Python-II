# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player(Room, Item):
    def __init__(self,name, Room):
        super().__init__()
        self.name = name
        self.current_room = Room
        self.items = []


