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

