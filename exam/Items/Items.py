class Items:

    items = []

    def __init__(self,name):
        self.name= name
    def __str__(self):
        return f"{self.name}"

    def take_item(self):
        Items.items.append(self.name)



    def backpack():
        return Items.items

    def use_item(self):
        if self in Items.items:
            print(f"You use {self}")
        else:
            print(f"You dont have {self}")