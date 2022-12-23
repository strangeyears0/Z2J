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

#ex2
# number = 3
# user_input=int(input("I'm Thinking of a number between 1 and 10. Guess wich one"))
#
# if user_input == number:
#     print("You win")
# else:
#     print("You lose")

#8.4
# DISPLAY ALL THE FACTORS OF A NUMBER CHOSEN BY THE USER:
#
# num = int(input("Enter a positive intiger:\n"))
# for divisor in range(1, num + 1):
#     if num % divisor == 0:
#         print(f"{divisor} is a factor of {num}")

#8.5
# Break out of the pattern

# sum_of_evens = 0
# for n in range(101):
#     if n % 2 == 0:
#         sum_of_evens = sum_of_evens + n
# print(sum_of_evens)

# break
# for n in range(4):
#     if n == 2:
#         break
#     print(n)
# print(f"Finished with n = {n}")

#continue

# for i in range(4):
#     if i == 2:
#         continue
#     print(i)
# print(f"Finished with i = {i}")

# for...else loops

# phrase = " it marks the spot"
#
# for character in phrase:
#     if character == "X":
#         break
# else:
#     print("There was no X")


# for n in range(3):
#     password = input("Password:\n")
#     if password == "I<3Fuck":
#         break
#     print("Password is incorrect")
# else:
#     print("Suspicious activity. The authorities have been alerted")

# exercises1
# while True:
#     user_input = input("Type 'q or 'Q' to quit:\n ")
#     if user_input.upper() == "Q":
#         break

# exercises2

# for i in range(1, 51):
#     if i % 3 == 0:
#         continue
#     print(i)

# 8.6 Recover from errors

# try and except keywords


# try:
#     number = int(input("Entre an intiger:"))
# except ValueError:
#     print("That was not a intiger")
#


# def divide(num1, num2):
#     try:
#         print(num1/num2)
#     except TypeError:
#         print("Both arguments must be numbers")
#     except ZeroDivisionError:
#         print("num 2 must not be 0")
# divide(1,2)


# ex1
# while True:
#     try:
#         user_input=int(input("Input intiger"))
#         print(f"Your intiger :\n{user_input}")
#     except ValueError:
#         print("that was not a intiger")
#         print("try again")

# ex2
#
# user_input_string=input("Input string.")
# try:
#     user_input_int=int(input("Input int."))
#     print(user_input_string[user_input_int])
# except ValueError:
#     print("Invalid number")
# except IndexError:
#     print("Index is out of bonds")

#8.7 Simulate events and calculate probabilities

# import random
#
# randint=(random.randint(1,3))
# print(randint)

#FAIR COINS

# import random
#
# def coin_flip():
#     """Random return heads or tails"""
#     if random.randint(0,1) == 0:
#         return "heads"
#     else:
#         return "tails"
#
# heads_tally = 0
# tails_tally = 0
#
# for trial in range(1_000_000):
#     if coin_flip() == "heads":
#         heads_tally = heads_tally +1
#     else:
#         tails_tally = tails_tally +1
# ratio = heads_tally/tails_tally
# print(f"Ratio is: {ratio:.3f}")
#
#

#UNFAIR Coins

# import random
#
# def unfair_coin_flip(probality_of_tails):
#     """Unfair return random"""
#     if random.random() < probality_of_tails:
#         return "tails"
#     else:
#         return "heads"
# heads_tally = 0
# tails_tally = 0
#
# for trial in range(10_000):
#     if unfair_coin_flip(.9) == "heads":
#         heads_tally = heads_tally + 1
#     else:
#         tails_tally = tails_tally + 1
# ratio = heads_tally / tails_tally
# print(f"The ratio of heads to tails is {ratio:.3f}")


#exercises1
# import random
#
# def roll():
#     """SIMULATE ROLLIG DIE"""
#     dieroll=random.randint(1,6)
#     print(f"You throw {dieroll}")
# roll()

#exercises2
#
# from random import randint
# def roll():
#     return randint(1,6)
# num_rolls = 100000
# total = 0
# for trial in range(num_rolls):
#     total = total + roll()
# avg_roll = total/ num_rolls
# print(f"The average result of {num_rolls} rolls is {avg_roll}")

#8.8 Challange simulate a coin toss experiments
# import random
#
# def single_trial():
#     """Simulate repeatedly a coing until both heads and tails are seen"""
#
#     flip_result = random.randint(0,1)
#     flip_count = 1
#
#     while flip_result == random.randint(0,1):
#         flip_count = flip_count + 1
#     flip_count = flip_count + 1
#     return flip_count

# def flip_trial_avg(num_trials):
#     """Calculate the avarage number of flips per trial over num+trials total trials."""
#     total = 0
#     for trial in range(num_trials):
#         total = total + single_trial()
#     return total / num_trials
#
# print(f"The avarege number of coin flips was {flip_trial_avg(10_000)}")

# 8.9
#
# from random import random
#
# num_times_A_wins = 0
# num_times_B_wins = 0
#
# num_trials = 10_000
# for trial in range(0, num_trials):
#     votes_for_A = 0
#     votes_for_B = 0
#
#     if random()<0.87:
#         votes_for_A = votes_for_A + 1
#     else:
#         votes_for_B = votes_for_B + 1
#
#     if random()<0.65:
#         votes_for_A = votes_for_A + 1
#     else:
#         votes_for_B = votes_for_B + 1
#     if random()<0.17:
#         votes_for_A = votes_for_A + 1
#     else:
#         votes_for_B = votes_for_B + 1
#
#     if votes_for_A > votes_for_B:
#         num_times_A_wins = num_times_A_wins + 1
#     else:
#         num_times_B_wins = num_times_B_wins + 1
#
# print(f"Probability A wins: {num_times_A_wins/num_trials}")
# print(f"Probability B wins: {num_times_B_wins/num_trials}")

# 9 Tuples, LIsts and Dictionaries
#
# my_first_tuple = (1, 2, 3)
# print(type(my_first_tuple))
# empty_tuple=()
# print(empty_tuple)
# #one element tuple"
# x=(1, )
# print(type(x))
# #built in tuple()
# print(tuple("Python"))
# numbers=(1, 2, 3)
# print(len(numbers))
#
# values= (1, 3, 5, 7, 9)
# print(values[2])
# print(values[2:4])
#
#
# # values[0]=2 type error
#
# # tuples are iterable
#
# vowels = ('u', 'i', 'o', 'a', 'q')
# for vowel in vowels:
#     print(vowel.upper())
#
# #tuplep packing and unpacking
# coordinats = 4.21, 9.23
# x,y = coordinats
# print(x)
# print(y)
#
# name, age, ocupation = "David", 34, "programmer"
# print(name, age, ocupation)
#
# # a, b, c, d = 1, 2,3 VALUE ERROR
#
# vowels = ('u', 'i', 'o', 'a', 'q')
# print('o' in vowels)
# print('x' in vowels)
#
# # Returning multiple values from a function
#
# def adder_substractot(num1,num2):
#     return (num1+num2, num1-num2)
# print(adder_substractot(3,2))

# exercises1

# cardinal_numbers = ("first", "second", "third")
# print(cardinal_numbers)
# # ex2
# print(cardinal_numbers[1])
# # ex3
# position1, position2, position3 = cardinal_numbers
# print(f"{position1}\n{position2}\n{position3}")
# #ex 4
# my_name = input(("My name"))
# # ex5
# tuple_name = (tuple(my_name))
# if 'x' in tuple_name:
#     print('x is in your name')
# else:
#     print("'x is not in your name")
# # ex6
# print(tuple_name[1:])

#9.2  Lists are mutable sequences
#
# colors= ["red", "yellow", "green", "blue"]
# print(type(colors))
# print(colors)
# built_in_list=list((1,2,3))
# print(built_in_list)
# built_in_list2=list('Python')
# print(built_in_list2)
# groceries = "eggs, milk, cheese"
# grocery_list = groceries.split(",")
# print(grocery_list)
# split_list="a;b;c"
# split_list=split_list.split(";")
# print(split_list)
# split_spaces= "the quick brown cow"
# split_spaces= split_spaces.split(" ")
# print(split_spaces)
# split_characters = "abbaabba"
# split_characters = split_characters.split("ba")
# print(split_characters)


# Basic list operators
#
# numbers=[1,2,3,4]
# print(numbers[1])
# print(numbers[1:3])
# check = "bob" in numbers
# print(check)
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# Changing elements in list
#
# colors  = ["red", "yellow", "green", "blue"]
# colors[0] = "burgundy"
# print(colors)
#
# colors[1:3] = ["orange", "magenta"]
# print(colors)
#
# colors  = ["red", "yellow", "green", "blue"]
# colors[1:3]=["orange","magenta","aqua"]
# print(colors)
#
# colors[1:4] = ["yellow","green"]
# print(colors)

# list methods for adding and removing elements

# list.insert()
#
# colors=["red","yellow","green","blue"]
# colors.insert(1,"orange")
# print(colors)
# colors.insert(10,"violet")
# print(colors)
# colors.insert(-1,"indigo")
# print(colors)
#
# # list.pop()
#
# color= colors.pop(3)
# print(color)
# color=colors.pop(-1)
# print(color)
# color=colors.pop()
# print(color)
#
# #list.append()
#
# color=colors.append("indigo")
# print(colors)
#
# # list.extend()
#
# colors.extend(["violet","ultraviolet"])
# print(colors)

# list of numbers
# nums = [1,2,3,4,5]
# total = 0
# for number in nums:
#     total = total + number
# print(total)
#
# sum = sum(nums)
# print(sum)
# min = min(nums)
# print(min)
# max = max(nums)
# print(max)

# list comprehensions

# numbers = (1, 2, 3, 4, 5)
# squares = [num**2 for num in numbers]
# print(squares)
#
# str_numbers = ["1.5", "2.3", "5.25"]
# float_numbers = [float(value) for value in str_numbers]
# print(float_numbers)


# exercises1:5
# food = ["rice", "beans"]
# print(food)
# food.append("broccoli")
# print(food)
# food.extend(["bread","pizza"])
# print(food)
# print(food[:2])
# print(food[-1])
# exercises6:8
# breakfast = "eggs, fruit, orange juice"
# list_breakfast= breakfast.split(",")
# print(list_breakfast)
# print(len(list_breakfast))
#
# lenghts=[len(item) for item in list_breakfast]
# print(lenghts)


# 9.3 Nesting Copying and sorting types and lists

# nesting list and tuples

# two_by_two = [[1,2], [3,4]]
# len=len(two_by_two)
# print(len)
# print(two_by_two[0])
# print(two_by_two[1])
# print(two_by_two[1][0])


# copying a list

# animals = ["lion","tiger"]
# large_cats = animals
# large_cats.append("Tigger")
# print(animals)

# animals = ["lion","tiger"]
# large_cats = animals[:]
# large_cats.append("leopard")
# print(large_cats)
# print(animals)
#
# import copy
#
# matrix1 = [[1,2], [3,4]]
# matrix2 = matrix1[:]
# matrix2[0] = [5,6]
# # print(matrix2)
# # print(matrix1)
# matrix2[1][0] = 1
# # print(matrix2)
# # print(matrix1)
#
# # deepcopy
#
# matrix3 = copy.deepcopy(matrix1)
# matrix3[1][0] = 3
# print(matrix3)
# print(matrix1)

# sorting list

# .sort()

# colors = ["red", "yellow", "green", "blue"]
# colors.sort()
# print(colors)
# numbers = [1,10,5,4]
# numbers.sort()
# print(numbers)
# colors = ["red", "yellow", "green", "blue"]
# colors.sort(key=len)
# print(colors)

# get second element

#
# def get_second_element(item):
#     return item[1]
# items = [(4,1),(1,2),(-9,0)]
# items.sort(key=get_second_element)
# # print(items)