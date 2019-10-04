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


    def add_item(self, item):
        self.items.append(item)

    def get_player_items(self):
        room_str = f"\t{self.name}'s items: \n"
        for i in range(len(self.items)):
            room_str += f"\t[{i}]:\t[{self.items[i].name}] - {self.items[i].description}\n"
        return room_str
