from help import help
from Room1.Room1 import room1


print("\tWelcome in my game.\n"
      "1.--START--\n"
      "2.--HELP--\n"
      "3.--QUIT--\n")
a = input("Change number\n")
if a == "1":
    room1()

if a == "2":
    help()

if a == "3":
    quit()
