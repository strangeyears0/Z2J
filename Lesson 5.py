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

# exercises1,2

# data = ((1, 2), (3, 4))
# index=1
# for row in data:
#
#     print(f"Row {index} sum: {sum(row)}")
#     index +=1

#ex3,4,5
# variable_numbers = [4, 3, 2, 1]
# # copy_variable_numbers=variable_numbers[:]
# # print(copy_variable_numbers)
# print(variable_numbers)
# variable_numbers.sort()
# print(variable_numbers)

#9.4Challange: list of lists

#
# def enrollment_stats(list_of_universities):
#     total_students = []
#     total_tution = []
#
#     for university in list_of_universities:
#         total_students.append(university[1])
#         total_tution.append(university[2])
#
#     return total_students, total_tution
#
# def mean(values):
#     return sum(values) / len(values)
#
# def median(values):
#     values.sort()
#     if len(values) % 2 == 1:
#         center_index = int(len(values) / 2)
#         return values[center_index]
#     else:
#         left_center_index = (len(values) - 1) // 2
#         right_center_index = (len(values) + 1) // 2
#         return mean([values[left_center_index], values[right_center_index]])
#
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]
# totals = enrollment_stats(universities)
#
# print("\n")
# print("****" * 6)
# print(f"Total students: {sum(totals[0]):}")
# print(f"Total tuitions :  $ {sum(totals[1]):}")
# print(f"\n Students mean: {mean(totals[0]):,.2f} ")
# print(f"Student median: {median(totals[0]):}")
# print(f"\n Tution mean: $ {mean(totals[1]):,.2f} ")
# print(f"Tutin median:  $ {median(totals[1]):}")
#


# 9.5 challange

# import random
# noun = [
#     "kot",
#     "drzewo",
#     "komputer",
#     "samochód",
#     "dom",
#     "książka",
#     "telefon",
#     "krzesło",
#     "biurko",
#     "ołówek",
#     "osoba",
#     "miasto",
#     "rzeka",
#     "morze",
#     "góra",
#     "las",
#     "słońce",
#     "księżyc",
#     "gwiazdy",
#     "chmury",
#     "deszcz",
#     "śnieg",
#     "wiatr",
#     "burza",
#     "szklanka",
#     "talerz",
#     "sztućce",
#     "kubek",
#     "garnek",
#     "patelnia",
#     "piekarnik",
#     "lodówka",
#     "zlew",
#     "umywalka",
#     "prysznic",
#     "wanna",
#     "ubikacja",
#     "pralka",
#     "suszarka",
#     "odkurzacz",
#     "mop",
#     "szczotka",
#     "mydło",
#     "pasta do zębów",
#     "szampon",
#     "dezodorant",
#     "perfumy",
#     "krem",
#     "balsam do ciała",
#     "płyn do mycia naczyń",
#     "płyn do prania",
#     "proszek do prania",
#     "sól",
#     "pieprz",
#     "cukier",
#     "olej",
#     "mąka",
#     "jajka",
#     "mleko",
#     "masło",
#     "ser",
#     "chleb",
#     "ciasto",
#     "ciastka",
#     "lody",
#     "owoce",
#     "warzywa",
#     "mięso",
#     "ryby",
#     "kurczak",
#     "indyk",
#     "kaczka",
#     "królik",
#     "owca",
#     "koń",
#     "krowa",
#     "świnia",
#     "kura",
#     "gęś",
#     "kaczka",
#     "dziadek",
#     "babcia",
#     "ojciec",
#     "matka",
#     "syn",
#     "córka",
#     "brat",
#     "siostra",
#     "dziadek",
#     "babcia",
#     "chłopiec",
#     "dziewczynka",
#     "mężczyzna",
#     "kobieta",
#     "starszy pan",
#     "starsza pani",
#     "chłopiec",
#     "dziewczynka",
#     "mężczyzna",
#     "kobieta",
# ]
# verb = [
#     "lubić",
#     "kochać",
#     "uwielbiać",
#     "cieszyć się",
#     "marzyć",
#     "myśleć",
#     "mówić",
#     "słuchać",
#     "patrzeć",
#     "widzieć",
#     "szukać",
#     "znajdować",
#     "posiadać",
#     "mieć",
#     "chcieć",
#     "potrzebować",
#     "pragnąć",
#     "życzyć sobie",
#     "próbować",
#     "kosztować",
#     "smakować",
#     "lubić",
#     "kochać",
#     "uwielbiać",
#     "cieszyć się",
#     "marzyć",
#     "myśleć",
#     "mówić",
#     "słuchać",
#     "patrzeć",
#     "widzieć",
#     "szukać",
#     "znajdować",
#     "posiadać",
#     "mieć",
#     "chcieć",
#     "potrzebować",
#     "pragnąć",
#     "życzyć sobie",
#     "próbować",
#     "kosztować",
#     "smakować",
#     "iść",
#     "chodzić",
#     "biegać",
#     "jeździć",
#     "latać",
#     "pływać",
#     "nurkować",
#     "skakać",
#     "bawić się",
#     "zabawać",
#     "śpiewać",
#     "grać",
#     "tańczyć",
#     "rysować",
#     "malować",
#     "pisać",
#     "czytać",
#     "uczyć się",
#     "studiować",
#     "pracować",
#     "odpoczywać",
#     "relaksować się",
#     "spać",
#     "budzić się",
#     "myć",
#     "czesać",
#     "ubierać",
#     "rozbierać",
#     "jeść",
#     "pić",
#     "oddychać",
#     "mruczeć",
#     "szczekać",
#     "miauczeć",
#     "szczekać",
#     "świergotać",
#     "kwilić",
#     "pieścić",
#     "głaskać",
#     "przytulać",
#     "całować",
#     "objąć",
#     "trzymać",
#     "uściskać",
#     "pocałować",
#     "przytulić",
#     "głaskać po głowie",
#     "masować",
#     "przytulać",
#     "kochać się",
#     "całować",
#     "przytulać",
#     "głaskać",
#     "masować",
#     "trzymać za rękę",
#     "całować w rękę",
#     "przytulać do siebie",
#
# ]
#
# adjective =[
#     "piękny",
#     "ładny",
#     "cudowny",
#     "wspaniały",
#     "doskonały",
#     "fantastyczny",
#     "niesamowity",
#     "zjawiskowy",
#     "wyjątkowy",
#     "niezwykły",
#     "ciepły",
#     "zimny",
#     "gorący",
#     "chłodny",
#     "ciekawy",
#     "interesujący",
#     "fascynujący",
#     "zajmujący",
#     "wciągający",
#     "pasjonujący",
#     "długi",
#     "krótki",
#     "wysoki",
#     "niski",
#     "szeroki",
#     "wąski",
#     "gruby",
#     "cienki",
#     "tłusty",
#     "chudy",
#     "młody",
#     "stary",
#     "nowy",
#     "stary",
#     "używany",
#     "świeży",
#     "zepsuty",
#     "sprawny",
#     "niesprawny",
#     "wygodny",
#     "niewygodny",
#     "komfortowy",
#     "niekomfortowy",
#     "elegancki",
#     "nieelegancki",
#     "modny",
#     "niemodny",
#     "szykowny",
#     "nieszykowny",
#     "oryginalny",
#     "nieoryginalny",
#     "prawdziwy",
#     "fałszywy",
#     "autentyczny",
#     "nieautentyczny",
#     "prawdziwy",
#     "fałszywy",
#     "autentyczny",
#     "nieautentyczny",
#     "dobry",
#     "zły",
#     "miły",
#     "niemiły",
#     "przyjemny",
#     "nieprzyjemny",
#     "sympatyczny",
#     "niesympatyczny",
#     "miłosny",
#     "niemiłosny",
#     "przyjacielski",
#     "nieprzyjacielski",
#     "przyjazny",
#     "nieprzyjazny",
#     "lojalny",
#     "nielojalny",
#     "wierny",
#     "niewierny",
#     "oddany",
#     "nieoddany",
#     "podejrzliwy",
#     "nieufny",
#     "ostrożny",
#     "nieostrożny",
#     "czujny",
#     "nieczujny",
#     "ostrożny",
#     "nieostrożny",
#     "ostrożny",
#     "nieostrożny",
#     "bezpieczny",
#     "niebezpieczny",
#     "ryzykowny",
#     "bezpieczny",
#     "niebezpieczny",
#     "ryzykowny",
#     "bezpieczny",
#     "niebezpieczny",
# ]
#
# preposition = [
#     "nad",
#     "pod",
#     "przed",
#     "za",
#     "obok",
#     "pomiędzy",
#     "wśród",
#     "podczas",
#     "po",
#     "przed",
#     "zaraz po",
#     "zanim",
#     "po tym jak",
#     "od",
#     "do",
#     "z",
#     "za pośrednictwem",
#     "zgodnie z",
#     "według",
#     "wbrew",
#     "przeciwko",
#     "na",
#     "na rzecz",
#     "wspólnie z",
#     "wraz z",
#     "w obecności",
#     "bez",
#     "przy",
#     "blisko",
#     "daleko",
#     "gdzieś",
#     "kiedyś",
#     "kiedykolwiek",
#     "nigdy",
#     "zawsze",
#     "prawie",
#     "niemal",
#     "już",
#     "jeszcze",
#     "wciąż",
#     "znowu",
#     "ponownie",
#     "od nowa",
#     "na nowo",
#     "za każdym razem",
#     "zawsze",
#     "często",
#     "rzadko",
#     "kilka razy",
#     "wiele razy",
#     "niektóre razy",
#     "niekiedy",
#     "prawie zawsze",
#     "prawie nigdy",
#     "zazwyczaj",
#     "zwykle",
#     "przeważnie",
#     "najczęściej",
#     "najrzadziej",
#     "niezbyt często",
#     "rzadko",
#     "bardzo rzadko",
#     "prawie zawsze",
#     "prawie nigdy",
#     "zazwyczaj",
#     "zwykle",
#     "przeważnie",
#     "najczęściej",
#     "najrzadziej",
#     "niezbyt często",
#     "rzadko",
#     "bardzo rzadko",
#     "między",
#     "wśród",
#     "wewnątrz",
#     "na zewnątrz",
#     "poza",
#     "na końcu",
#     "na początku",
#     "na górze",
#     "na dole",
#     "na lewo",
#     "na prawo",
#     "do góry",
#     "w dół",
#     "w lewo",
#     "w prawo",
#     "w przód",
#     "w tył",
#     "do przodu",
#     "do tyłu",
#     "w stronę",
#     "w kierunku",
#     "na wprost",
#     "naprzeciwko",
#     "blisko",
#     "daleko",
#     "obok",
#     "przy",
#     "za",
# ]
#
# adverb = [
#     "szybko",
#     "wolno",
#     "natychmiast",
#     "w końcu",
#     "ostatecznie",
#     "pewnie",
#     "ostrożnie",
#     "cicho",
#     "głośno",
# ]
#
# def make_poem():
#     n1 = random.choice(noun)
#     n2 = random.choice(noun)
#     n3 = random.choice(noun)
#     while n1 == n2:
#         n2 = random.choice(noun)
#     while n1 == n3 or n2 == n3:
#         n3 = random.choice(noun)
#
#     v1 = random.choice(verb)
#     v2 = random.choice(verb)
#     v3 = random.choice(verb)
#     while v1 == v2:
#         v2=random.choice(verb)
#     while v1 == v3 or v2 == v3:
#         v3 = random.choice(verb)
#
#     adj1= random.choice(adjective)
#     adj2= random.choice(adjective)
#     adj3= random.choice(adjective)
#     while adj1 == adj2:
#         adj2 = random.choice(adjective)
#     while adj1 == adj3 or adj2 == adj3:
#         adj3 = random.choice(adjective)
#
#
#     prep1=random.choice(preposition)
#     prep2=random.choice(preposition)
#     while prep1 == prep2:
#         prep2 =random.choice(preposition)
#
#     adv1 = random.choice(adverb)
#
#     poem = (
#         f"{adj1} {n1}\n\n"
#         f"{adj1} {n1} {v1} {prep1}  {adj2} {n2} \n"
#         f" {adv1} {n1} {v2}\n"
#         f"{n2} {v3} {prep2} {adj3} {n3}"
#
#     )
#     return poem
# poem = make_poem()
# print(poem)

#9.6 Store relationships in dictionaries
# creating dictionaries:

# capitals = {
#     "California":"Sacramento",
#     "New York":"Albamy",
#     "Texas":"Austin"
# }
# print(capitals)
#
#
# # built_in dict()
#
# key_value_pairs = (
#     ("california","sacramento"),
# )
# capitals = dict(key_value_pairs)
# print(capitals)
#
# # empty dict
# empty={}
# print(empty)
# print(dict())
#
# # accesing dictionary values
# capitals = {
#     "California":"Sacramento",
#     "New York":"Albamy",
#     "Texas":"Austin"
# }
#
# print(capitals["Texas"])
#
# # adding and removing values in a dictionary
#
# capitals["Colorado"]="Denver"
# print(capitals)
# capitals["Texas"]="Houston"
# print(capitals)
# del capitals["Texas"]
# print(capitals)
# #
# # checking the existance of dictionary keys
#
# print("Arizona" in capitals)
# print("California" in capitals)
#
# if "Arizona" in capitals:
#     print(f"The capitol of arizona is {capitals['Arizona']}")
#
# # iteratimg over dictionaries
#
# for key in capitals:
#     print(key)
#
# for state in capitals:
#     print(f"The capital of {state} is {capitals[state]}")
#
# # capital.items()
# for state, capital in capitals.items():
#     print(f"The capitol of {state} is {capital}")
# capitals[50]="Honolulu"
# print(capitals)

# # Nested dictionaries
#
# states = {
#     "California":{
#         "capital":"Sacramento",
#         "flower":"California Poppy"
#     },
#     "New York":{
#         "capital":"Albamy",
#         "flower":"rose"
#     },
# }
# print(states["California"])
# print(states["California"]["flower"])

# #exercises1.
# # ex2
# captains ={}
# captains["Enterprise"]="Picard"
# captains["Voyager"]="Janeway"
# captains["Defiant"]="Sisko"
#
# print(captains)
#
# # ex3
#
# if "Enterprise" not in captains:
#     captains["Enterprise"] = "uknown"
# if "Discovery" not in captains:
#     captains["Discovery"] = "uknown"
# for ship in["Enterprise","Discovery"]:
#     if not ship in captains:
#         captains[ship] = "uknown"
#
# #ex4
#
# for ship, captain in captains.items():
#     print(f"{ship} is captained by {captain}.")
# # ex5
# del captains["Discovery"]
# print(captains)
#
# #ex6
#
# captains =dict(
#     [
#         ("Enterprise","Picard"),
#         ("Voyager","Janeway"),
#         ("Defiant","Sisko"),
#     ]
# )
# print(captains)

#9.7

import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

state, capital = random.choice(list(capitals_dict.items()))

while True:
    guess = input(f"What is the capital of {state}?").lower()
    if guess == "exit":
        print(f"The capital of {state} is {capital}.")
        print("Goodbye")
        break
    elif guess == capital.lower():
        print("Correct ")
        break