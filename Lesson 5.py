# 8COndittional logic and control flow

# 8.1 Compare Values

# Boolean operators:
#
# <
# >
# >=
# <=
# !=
# ==
#

#exercises1

# print(1 <= 1)
# print(1 != 1)
# print(1 != 2)
# print('good' != "bad")
# print("good" != "Good")
# print(123 == "123")
#
# # ex2.

# print(3 != 4)
# print(10 > 5)
# print("jack" != "jill")
# print(42 != "42")


#8.2 Add some logic

# AND
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)


# OR
# print(True or True)
# print(True or False)
# print(False or True)
# # print(False or False)

# NOT
#
# print(not True)
# print(not False)

# Building complex EXPRESSIONS
# print(True and not (1 != 1))
#
# print(("A" != "A") or not (2 >=3 ))
#
# print(True and False == True and False)
# print((True and False) == (True and False))

#exercises1
# print((1 <= 1) and(1 != 1))
# print(not(1 != 2))
# print(("good" != "bad") or False)
# print(("good" != "Good") and not (1 == 1))

#exercises2

# print(False == (not True))
# print((True and False) == (True and False))
# print(not (True and "A" == "B"))


#8.3 Control the flow of your programms
# the IF statement
#
# if 2+2 == 4:
#     print("2 and 2 is 4")
#
# grade = 50
# if grade >= 70:
#     print("You passed")
# if grade < 70:
#     print("Tou not passed")
# print("This your for attendig")

# else keyword

# grade = 40
#
# if grade >= 70:
#     print("you passed")
# else:
#     print("you dont pass")
# print("No elo")

# elif keyword

# grade = 70
#
# if grade >=90:
#     print("You pass with A")
# elif grade >=80:
#     print("You pass with B")
# elif grade >=70:
#     print("You pass with C")
# else:
#     print("You dont pass")
# print("Thank you")

#nested if statemnest

# sport = input("Enter a sport")
# p1_score = int(input("Enter player 1 score"))
# p2_score = int(input("Enter player 2 score"))
#
# if sport.lower() == "basketball":
#     if p1_score == p2_score:
#         print("Draw")
#     elif p1_score > p2_score:
#         print("1 WIN")
#     else:
#         print("2 WIN")
# elif sport.lower() == "golf":
#     if p1_score == p2_score:
#         print("Draw")
#     elif p1_score < p2_score:
#         print("1 WIN")
#     else:
#         print("2 WIN")
# else:
#     print("Uknow sport")

#REFACTOR


# sport = input("Enter a sport")
# p1_score = int(input("Enter player 1 score"))
# p2_score = int(input("Enter player 2 score"))
#
# sport = sport.lower()
# if p1_score == p2_score:
#     print("The game is a draw")
# elif (sport == "basketball") or (sport == "golf"):
#     p1_wins_bbal = (sport == "basketball") and (p1_score > p2_score)
#     p1_wins_golf = (sport == "golf") and (p1_score < p2_score)
#     p1_wins = p1_wins_bbal or p1_wins_golf
#     if p1_wins:
#         print("Player 1 Wins.")
#     else:
#         print("Player 2 wins.")
# else:
#     print("Uknown sport")

# exercises1

# user_input = input("Enter Word")
# word_length = len(user_input)
# if word_length == 5:
#     print("Your input is 5 character long")
# elif word_length > 5:
#     print("Your input is greater than 5 characters long")
# elif word_length < 5:
#     print("Your input is less than 5 characters long")

number = 3
user_input=int(input("I'm Thinking of a number between 1 and 10. Guess wich one"))

if user_input == number:
    print("You win")
else:
    print("You lose")
