# STRINGS AND STRING METHODS
#

# string = "What i'm doing? "
# print(string)
# string1 = 'Hello World'
# string2 = "1234"
#
# length = len(string1)
# print(length)

#multiline STRINGS (\)
#
# paragraph = "This string is very long problem is solved\
# becouse i can use this slash\
# and write code"
#
# print(paragraph)

# paragraph2 = '''I can also use this triple cudzyslow if i wanna
# multiline
# and
# long
# shit
#  but is no display on one line'''
#
# print(paragraph2)

#Indexing and slicing


#STRING CONCATENATION
#
# string1 = "abra"
# string2 = "cadabra"
# magic_string = string1 + string2
# print(magic_string)


#STRING Indexing
#
# string = "anything"
# print(string[1])
# print(string[5])
# print(string[-1])
# print(string[-1])
# print(string[0])
# user_input = 'anything'
# #
# # final_index = len(user_input) -1
# # last_character = user_input[final_index]
# # last_character = user_input[-1]
# # print(last_character)

#STRING slicing
#
# string = "anything is everything"
# first_word = string[0] + string[1] + string[2]
# print(first_word)
#

#substring
#
# string = "anything is everything"
# print(string[0:3])
#
# #note
# empty_string = ""
# non_empty_string = "   "

#STRINGS ARE IMMUTABLE
#
# word = "goal"
# word = "f" + word[1:]
# print(word)

#EXERCIES

#1.

# string = 'howlong'
# print(len(string))

#2.
#
# string1= "yerba"
# string2= "mate"
# string_full= string1 + string2
# print(string_full)

#3.
# string1= "yerba"
# string2= "mate"
# string_full= string1 + " "+ string2
# print(string_full)
#

#4.
# string='bazinga'
# print(string[2:6])


#4.3 MANIPULATE STRINGS WITH METODS

# name = "Jean-Luc Picard"
# print(name.lower())
# print(name.upper())
# print(len(name))

#REmove whitespaces

# name = "Jean-Luc Picard      "
# print(name.rstrip())
#
# name = "         Jean-Luc Picard"
# print(name.lstrip())
#
# name = "   Jean-Luc Picard      "
# print(name.strip())


#Determine if a string starts or ends with a particular string

# starship = "Enterprise"
# print(starship.startswith("en"))
# print(starship.startswith("En"))
# print(starship.endswith("ise"))

#STRINGS METHODS AND IMMUTABILITY

# name = 'Picard'
# name = name.upper()
# print(name)

#USING IDLE TO DSICOVER ADDITINAL STRING METHODS
#
# starship = "Enterpirse"
# starship.
#


#EXERCIsES
# 1.
# string1 = "Animals"
# string2 = "Badger"
# string3 = "Honey Bee"
# string4 = "Honey Badger"
#
# string1 = string1.lower()
# string2 = string2.lower()
# string3 = string3.lower()
# string4 = string4.lower()
#
# print(string1)
# print(string2)
# print(string3)
# print(string4)

#2

#
# string1 = "Animals"
# string2 = "Badger"
# string3 = "Honey Bee"
# string4 = "Honey Badger"
#
# string1 = string1.upper()
# string2 = string2.upper()
# string3 = string3.upper()
# string4 = string4.upper()
#
# print(string1)
# print(string2)
# print(string3)
# print(string4)


#3

# string1 = "      Filet Mignon"
# string2 = "Brisket      "
# string3 = "   Chees    "
#
# string1 = string1.lstrip()
# string2 = string2.rstrip()
# string3 = string3.strip()
#
# print(string1)
# print(string2)
# print(string3)
#

#4
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = "  bEautiful"
#
#
#
# string1 = string1.startswith("be")
# string2 = string2.startswith("be")
# string3 = string3.startswith("be")
# string4 = string4.startswith("be")
#
# print(string1)
# print(string2)
# print(string3)
# print(string4)

#5
#
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = "  bEautiful"
#
# string1 = string1.lower()
# string3 = string3.lower()
# string4= string4.lower().lstrip()
# string1 = string1.startswith("be")
# string2 = string2.startswith("be")
# string3 = string3.startswith("be")
# string4 = string4.startswith("be")
#
# print(string1)
# print(string2)
# print(string3)
# print(string4)


#4.4 Interact with user input

# propmpt = "Hey what's up?"
#
# user_input = input(propmpt)
#
#
# print(f"You said {user_input}")
#
# response = input("What should ia shout?")
# shouted_response = response.upper()
# print(f"Well y ou insist {shouted_response
# }")

#.1

# user_input = input("Napisz coś")
# print(user_input)

#.2

# user_input = input("Napisz coś:")
# user_input_lower = user_input.lower()
# print(user_input_lower)

#3.

# user_input = input("Napisz coś:")
# user_input_lower = user_input.lower()
# print(user_input_lower)
# print(len(user_input))

#4.5

#pick apart your user_input

# password  = input("Tell me your password")
# back = password[0].upper()
# print(f"The first letter your password is {back}")

#4.6 Working with strings and numbers

#using strings with arithmetic operators
#
# num = "2"
# print(num + num)
# print(num*3)
#
#Converting strings to numbers

# num = input("Enter number to doubled :\n")
# #num = int(num)
# num = float(num)
# doubled_num = num *2
# print(doubled_num)

#Converting numbers to strings

# num_panckaces = 10
# print("Im going to eat " + str(num_panckaces) + " panckackes." )

#ex
#1.
# string = '1'
# string = int(string)
# print(string*2)
#2.
# string = '1'
# string = float(string)
# print(string*2)
#3.
# string = '1'
# integer = 1
#
# print(str(integer))
# print(int(string))
#4.

# num_1 = input("Enter first number\n")
# num_2 = input("Enter second number\n")
# multiple = float(num_1) * float(num_2)
# print(multiple)

#4.7 Streamline Your Prints
# name="Andrzej"
# heads=2
# arms=4
# print(f"{name} has {heads} head and {arms} arms.To chyba jakiś jebany potwór")
#
# n=3
# m=4
# print(f"{n} times {m} is {n*m}")
#
# print("{} has {} and {} arms".format(name,heads,arms))

#EXERCIsES
#1,2,3
# weight=float(0.2)
# animal = "newt"
#
# print(str(weight) + " kg is the weight of the " + animal)
# print("{} kg is the weight of the {}".format(weight,animal))
# print(f"{weight} kg is the weight of  the {animal}")

#4.8

# Find a String in a string
# .find
# phrase = "the surprise is in here somewhere"
#
# print(phrase.find("surprise"))
# print(phrase.find("gówno"))
# print("i put string in your string".find("string"))
# print("my number is 555-555-555".find("5"))
#
# .replace
#
# my_story = "I'm telling you the truth: nothing but the truth"
# print(my_story.replace("the truth","lies"))
# my_story = my_story.replace("the truth","lies")
# print(my_story)
#
# text="some of the stuff"
# new_text = text.replace("some of","all")
# new_text = new_text.replace("stuff","things")
# print(new_text)

#ex1,2
# string = "AAA"
# print(string.find("a"))
#
# string= "Somebody said something to Samantha".replace("s","z")
# print(string)

# ex3

# user_input = input("Wpisz coś")
# print(user_input.find("a"))


#4.9

# user_input = input("Enter some text :\n")
# user_input = user_input.replace("a","4").replace("b","8").replace("e","3")\
#             .replace("l","1").replace("o","0").replace("s","5").replace("t","7")
# print(user_input)


#5 NUMBERS AND MATH

#5.1 Integers and Floating-points NUMBERS

#Integers

# print(type(1))
#
# num = 25 #intiger literal
#
# print(int("25"))
# print(1_000_000)

#Floating Points numbers

# print(type(1.0))
# print(float("1.25"))
# print(1000000.0)
# print(1_000_000.0)
# print(1e6)
# print(20000000000000000000.0)
# print(1e-4)
# print(2e400)
# n=2e400
# print(n)
# print(type(n))
# print(-2e400)
#exercises

# #1
# num1 = 25000000
# num2 = 25_000_000
# print(num1)
# print(num2)

#2

# num1 = 175e3
# print(num1)

#3

# print(2e307) #maks

#5.2 ARITHMETIC OPERATORS AND EXPRESSIONS


#addition
#
# print(1 + 2)
# print(1.0 + 2)
#
# #substration
#
# print(1 - 1)
# print(5.0 - 3)
# print(1 - (-3))
#
# #multiplication
#
# print(3 * 3)
# print(2 * 8.0)

#division

# print(9 / 3)
# print(5.0 / 2)
# print(
#     int(9 / 3)
# )
# print(
#     int(5.0 / 2)
# )

#Intiger division

# / intiger division
# // floor division
# print(
#     9//3
# )
# print(5.0//2)
# print(-3//2)

#EXPONENTS
# print(2**2)
# print(2**3)
# print(2**4)
# print(3**1.5)
# print(3**-1)
# print(2**-2)

#The modulus operator

# print(5 % 3)
# print(16 % 8)
# print(5 % -3)
# print(-5 % -3)

#artithmetic expresions

# print(2 * 3 -1)
# print(4 / 2 + 2**3)
# print(-1 +(-3 * 2 + 4))


#5.3

# num1 = input("Podaj pierwszą liczbę")
# num2 = input("podaj drugą liczbę")
#
# num1 = float(num1)
# num2 = float(num2)
#
# power = num1**num2
# print(f"{num1} do potęgi {num2} równa się {power}")