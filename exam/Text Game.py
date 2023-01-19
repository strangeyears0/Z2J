location = "room1"
def room1():
    file_path = "D:/Z2J/exam/room1.txt"
    file = open(file_path, mode="r", encoding= "utf-8")
    for line in file:
        print(line,end="")
def room2():
    file_path = "D:/Z2J/exam/room2.txt"
    file = open(file_path, mode="r", encoding= "utf-8")
    for line in file:
        print(line,end="")
def help():
    print(f"u-use item\n"
          f"t-take item\n"
          f"i-item list\n"
          f"h-help\n"
          f"d-describe room\n"
          f"l-go left\n"
          f"r-go right\n")
def describe_room1():
    return room1()
def describe_room2():
    return room2()
class Inventory:

    items = []

    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"{self.name}"

    def use_item(self):
        print(f"You use {self.name}")

    def take_item(self):

        Inventory.items.append(self.name)
        print(f"You take {self.name} ")
        print(f"You take {self.name} ")


def action():
    choice = input("\nEnter Choice")
    choice.lower()

    if choice == 't':
        item = input("Choose item to take:\n")
        item.lower()
        if location == "room1":
            if item == "rock":
                print(f"You take {item}")
                return Inventory(item).items.append(item), action()
            elif item == "paper":
                print(f"You take {item}")
                return Inventory(item).items.append(item), action()
            elif item == "glass":
                print(f"You take {item}")
                return Inventory(item).items.append(item), action()
            else:
                return print(f"There is no such {item} here"), action()
        else:
            print("Change location")
            return action()
    elif choice == 'i':
        print(f"Your Inventory:\n"
              f"Inventory.items")
        return action()
    elif choice == 'u':
        item = input("Choose item to use:\n")
        item.lower()
        if item == "rock":
            if item in Inventory.items:
                print(f"You use {item}")
                return action()
        else:
            print(f"You don't have {item}")
            return action()
    elif choice == 'h':
        return help(), action()

    elif choice == 'd':
        return describe_room1(), action()
    elif choice == 'l':
        location = "room2"
        if location == 'room2':

        return describe_room2(),action()
    else:
        print("Bad choice! Type h if you wanna help")
        return action()




help()
describe_room1()
action()
