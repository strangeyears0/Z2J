#6 function and loops
#6.1 what is a function really?

#NOTATKI W ZESZYCIE

#6.2
# WRITE YOUR OWN FUNCTIONS
# Calling a user definie
# def multiply(x,y): #SIGNATURE
#     #BODY
#     product = x * y
#     return product
# print(multiply(1,6))
#DOCUMENTING YOUR FUNCTIONS
# print(help(len))

# def multiply(x,y):
#     """Return the product of two numbers x and y"""
#     product = x * y
#     return product
#
# print(help(multiply))
#

#EXERCIsES
#1

# def cube(x):
#     """Return the third power x"""
#     product = x**3
#     return product
# print(cube(2))
# print(cube(3))
# print(help(cube))

#2
# def greet(name):
#     """Return greeting name"""
#     print(f"Hello {name}")
#
# print(greet("Bartek"))

#6.3 CONVERT TEMPERATURES

# celcius = input("Enter temperature in degrees C:")
# farenheit = input("Enter temperature in degrees F:")
# celcius = float(celcius)
# farenheit = float(farenheit)
#
#
# def convert_cel_to_far(celcius):
#     """ CONVERT CELCIUS TO FARENHEIT"""
#     F = celcius * 9/5 + 32
#     return F
#
# def convert_far_to_cel(farenheit):
#     """Convert fareheit to celcius"""
#     C = (farenheit - 32) * 5/9
#     return C
#
# print(f"{farenheit} degrees F is {convert_far_to_cel(farenheit):.2f} degrees C")
# print(f"{celcius} degrees C is {convert_cel_to_far(celcius):.2f} degrees F")


#6.4  Run in circles

#while loop
# n=1
# while n<=5:
#     print(n)
#     n = n+1

# for loop

# for letter in "python":
#     print(letter)

# SAME IN WHILE

# word = "Python"
# index= 0
# while index<len(word):
#     print(word[index])
#     index = index + 1


# for n in range(3):
#     print("Python")

# for n in range(10,20):
#     print(n*n)

# amount = float(input("Enter an amount: "))
#
# for num_people in range(2, 6):
#     print(f"{num_people} people: ${amount/num_people:,.2f} each")

#NESTED LOOPS

# for n in range(1, 4):
#     for j in range(4, 7):
#         print(f"n = {n} and j = {j}")

#exercises1
#
# for n in range(2,11):
#     print(n)

# exercises2

# index=2
# while index<=11:
#     print(index)
#     index += 1

#3.

# def doubles(num):
#     """Return result of multiplaying an input number by 2"""
#     return num * 2
# my_num = 2
# for i in range(0, 3):
#     my_num = doubles(my_num)
#     print(my_num)

#6.5    TRACK YOUR INVESTMENTS
#
# def invest(amount, rate, years):
#     """Display year on year growth on a iniitial investment"""
#     for year in range(1, years + 1):
#         amount = amount * (1 + rate)
#         print(f"Year {year}: $ {amount:,.2f}")
#
#
# amount = float(input("Enter amount: \n"))
# rate = float(input("Enter rate: \n"))
# years = int(input("Enter years:\n"))
#
#
# invest(amount,rate,years)

#6.6 Undesrstqand scope in python\


# x= "Hello world"
#
# def func():
#     x = 2
#     print(f"Inside 'func' x has the value {x}")
# func()
# print(f"Outside 'func' x has the value {x}")
# print("Hello world is gloal scope, '2' is local scope")

# Scope resolution

# x = 5
# def outer_func():
#     y = 3
#     def inner_func():
#         z = x + y
#         return z
#     return inner_func


# The LEGB rule

# Local
# Enclosing
# Global
# Built-In

