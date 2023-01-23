flag = []


def room1():
    file_path = "D:/Z2J/exam/room1.txt"
    file = open(file_path, mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")


def room2():
    file_path = "D:/Z2J/exam/room2.txt"
    file = open(file_path, mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")


def room3_denied():
    file_path = "D:/Z2J/exam/room3_denied.txt"
    file = open(file_path, mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")


def room3_accept():
    file_path = "D:/Z2J/exam/room3_accept.txt"
    file = open(file_path, mode="r", encoding="utf-8")
    for line in file:
        print(line, end="")


def end():
    print("You win the game !")


def help():
    print(f"u-use item\n"
          f"t-take item\n"
          f"i-item list\n"
          f"h-help\n"
          f"d-describe room\n"
          f"l-go left\n"
          f"r-go right\n"
          f"b-go back\n")


def describe_room1():
    return room1()


def describe_room2():
    return room2()


def describe_room3_denined():
    return room3_denied()


def describe_room3_accept():
    return room3_accept()


class Inventory:
    items = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def use_item(self):
        print(f"You use {self.name}")

    def take_item(self):
        Inventory.items.append(self.name)
        print(f"You take {self.name} ")
        print(f"You take {self.name} ")


def action_2():
    choice = input("\nEnter Choice")
    choice.lower()

    if choice == 't':
        item = input("Choose item to take:\n")
        item.lower()
        print("There is nothing to use here")
        return action_2()
    elif choice == 'i':
        print(f"Your Inventory:\n"
              f"{Inventory.items}")
        return action_2()
    elif choice == 'u':
        item = input("Choose item to use:\n")
        item.lower()
        if item == "paper":
            if item in Inventory.items:
                print(f"You use {item}\n"
                      f"You ser fire to a page of the bible,"
                      f"a figure stretched out before you\n"
                      f"you can go back ! \n"
                      )
                flag.append('1')
                return action_2()

        else:
            print(f"You can't use {item} here")
            return action_2()
    elif choice == 'h':
        return help(), action_2()

    elif choice == 'd':
        return describe_room2(), action_2()
    elif choice == 'b':
        print("You go back")
        return describe_room1(), action()
    else:
        print("Bad choice! Type h if you wanna help")
        return action_2()



def action():
    choice = input("\nEnter Choice")
    choice.lower()

    if choice == 't':
        item = input("Choose item to take:\n")
        item.lower()

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

    elif choice == 'i':
        print(f"Your Inventory:\n"
              f"{Inventory.items}")
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
        return describe_room2(), action_2()
    elif choice == 'r':
        if '1' in flag:
            return describe_room3_accept(), action_3_accept()
        else:
            return describe_room3_denined(), action_3_denied()
    else:
        print("Bad choice! Type h if you wanna help")
        return action()


def action_3_denied():
    choice = input("\nEnter Choice")
    choice.lower()
    if choice == 't':
        item = input("Choose item to take:\n")
        item.lower()
        print("There is nothing to use here")
        return action_3_denied()
    elif choice == 'i':
        print(f"Your Inventory:\n"
              f"{Inventory.items}")
        return action_3_denied()

    elif choice == 'u':
        item = input("Choose item to use:\n")
        item.lower()

        if item in Inventory.items:
            print(f"You can't use {item}")
            return action_3_denied()
        else:
            print(f"You don't have {item}")
            return action_3_denied()
    elif choice == 'h':
        return help(), action_3_denied()

    elif choice == 'd':
        return describe_room3_denined(), action_3_denied()
    elif choice == 'b':
        print("You go back")
        return describe_room1(), action()
    else:
        print("Bad choice! Type h if you wanna help")
        return action_3_denied()


def action_3_accept():
    choice = input("\nEnter Choice")
    choice.lower()

    if choice == 't':
        item = input("Choose item to take:\n")
        item.lower()
        print("There is nothing to use here")
        return action_3_accept()
    elif choice == 'i':
        print(f"Your Inventory:\n"
              f"{Inventory.items}")
        return action_3_accept()
    elif choice == 'u':
        item = input("Choose item to use:\n")
        item.lower()
        if item == "rock":
            if item in Inventory.items:
                print(f"You throw {item}\n"
                      f"The cross hits the ground with impetus!\n"
                      f"The energy stored in it explodes,\n"
                      f" creating an exit to the surface.\n"
                      f"\tYOU ARE FREE"
                      )

                return end()
            else:
                print(f"You don't have {item}")
                return action_3_accept()
        else:
            print(f"You can't use {item} here")
            return action_3_accept()
    elif choice == 'h':
        return help(), action_3_accept()

    elif choice == 'd':
        return describe_room3_accept(), action_3_accept()
    elif choice == 'b':
        print("You go back")
        return describe_room1(), action()
    else:
        print("Bad choice! Type h if you wanna help")
        return action_3_accept()

help()
describe_room1()
action()
