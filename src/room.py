# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room():
    def __init__(self,name, description):
        self.name = name
        self.description = description
        self.n_to = []
        self.s_to = []
        self.e_to = []
        self.w_to = []
        self.items = []

    def __str__(self):
        return f"name: {self.name}"

    def add_item(self, item):
        self.items.append(item)



# r = Room("name", "description")

# i = Item("name", "des")
# r.add_item(i)
# print(r.items)