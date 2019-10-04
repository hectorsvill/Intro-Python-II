# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f"{self.name} : {self.description}"

    def add_item(self, item):
        self.items.append(item)

    # turn room items to string 
    def get_room_items(self, room):
        room_str = "\titems: \n"
        for i in range(len(self.items)):
            room_str += f"\t[{i}]:\t[{self.items[i].name}] - {self.items[i].description}\n"
        return room_str


    def del_item(self, item):
        self.items.remove(item)

# r = Room("name", "description")

# i = Item("name", "des")
# r.add_item(i)
# print(r.items)