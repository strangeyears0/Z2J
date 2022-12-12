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

