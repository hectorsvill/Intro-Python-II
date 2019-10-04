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
        return f"{self.name} - {self.description}"

    def add_item(self, item):
        self.items.append(item)



# r = Room("name", "description")

# i = Item("name", "des")
# r.add_item(i)
# print(r.items)