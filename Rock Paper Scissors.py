import random
def single_player():
    """Single player rock paper scissors"""
    choice=(1,2,3)
    computer_choice = random.choice(choice)

    while True:
        try:
            user_choice = int(input("Choose weapon (1,2,3):\n"
                                    "1.Rock\n"
                                    "2.Paper\n"
                                    "3.Scissors\n"
                                    "4.EXIT\n"))
        except ValueError:
            print("Choose 1,2,3 or 4")
            continue
        if user_choice == computer_choice:
            print(f"Computer choice {computer_choice}\n ")
            print("Draw")
            break
        elif user_choice == 1 and computer_choice == 2:
            print(f"Computer choice {computer_choice}\n"
                  f"Paper beat Rock")
            print("You loose")
            break
        elif user_choice == 1 and computer_choice == 3:
            print(f"Computer choice {computer_choice}\n"
                  f"Rock beat Scissors")
            print("You Win")
            break
        elif user_choice == 2 and computer_choice == 3:
            print(f"Computer choice {computer_choice}\n"
                  f"Scissors beat Paper")
            print("You loose")
            break
        elif user_choice == 2 and computer_choice == 1:
            print(f"Computer choice {computer_choice}\n"
                  f"Paper beat Rock")
            print("You Win")
            break
        elif user_choice == 3 and computer_choice == 1:
            print(f"Computer choice {computer_choice}\n"
                  f"Rock beat Scissors")
            print("You loose")
            break
        elif user_choice == 3 and computer_choice == 2:
            print(f"Computer choice {computer_choice}\n"
                  f"Scissors beat Paper")
            print("You Win")
            break
        elif user_choice == 4:
            print("Good Bye")
            break
def multi_player():
    """Multi player rock scisors paper"""
    while True:

        try:

            user1_choice = int(input("Player 1 Choose weapon  (1,2,3):\n"
                                    "1.Rock\n"
                                    "2.Paper\n"
                                    "3.Scissors\n"
                                    "4.EXIT\n"))
            user2_choice = int(input("Player 2 Choose weapon (1,2,3):\n"
                                    "1.Rock\n"
                                    "2.Paper\n"
                                    "3.Scissors\n"
                                    "4.EXIT\n"))
        except ValueError:
            print("Choose 1,2,3,4")
            continue
        if user1_choice ==4 and user2_choice ==4:
            print("Good Bye")
            break
        if user1_choice == user2_choice:
            print(f"User 2 Choice {user2_choice}\n ")
            print("Draw")
            break
        elif user1_choice == 1 and user2_choice == 2:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Paper beat Rock")
            print("Player 2 Win")
            break
        elif user1_choice == 1 and user2_choice == 3:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Rock beat Scissors")
            print("Player 1 Win")
            break
        elif user1_choice == 2 and user2_choice == 3:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Scissors beat Paper")
            print("Player 2 Win")
            break
        elif user1_choice == 2 and user2_choice == 1:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Paper beat Rock")
            print("Player 1 Win")
            break
        elif user1_choice == 3 and user2_choice == 1:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Rock beat Scissors")
            print("Player 2 Win")
            break
        elif user1_choice == 3 and user2_choice == 2:
            print(f"User 2 Choice {user2_choice}\n"
                  f"Scissors beat Paper")
            print("Player 1 Win")
            break
        elif user1_choice or user2_choice == 4:
            print("Good Bye")
            break
def menu():
    flag= True
    while flag:
        print("\t\t-----ROCK PAPER SCISSORS-----\n"
              "1.SINGLE PLAYER\n"
              "2.MULTIPLAYER\n"
              "3.EXIT")
        try:
            menu_choice=int(input("Please choose the game:\n"))
            if menu_choice == 1:
                single_player()
            elif menu_choice == 2:
                multi_player()
            elif menu_choice == 3:
                flag=False

                print("Good Bye")
                break

        except ValueError:
            print("Choose 1, 2 or 3")
            continue
menu()