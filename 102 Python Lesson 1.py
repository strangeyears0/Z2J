# OOP OBJECTED-ORIENTED PROGRAMING
#
# 10.1 DEFINIE A CLASS

# class Dog:
#
#     species = "Canis familiars"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# buddy = Dog("Buddy",9)
# miles = Dog("Miles",4)
# print(buddy.name)
# print(buddy.age)
# print(miles.name)
# print(miles.age)
# print(buddy.species)
#
# #Dynamic changes
#
# buddy.age = 10
#
# print(buddy.age)
# miles.species = "Shorthair dog"
# print(miles.species)

#instance methods


# class Dog:
#
#     species = "Canis familiars"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# buddy = Dog("Buddy",9)
# miles = Dog("Miles",4)
#
# print(miles)
# print(miles.speak("Woof Woof"))


# exercise1

# class Dog:
#
#     species = "Canis familiars"
#
#     def __init__(self, name, age, coat):
#         self.name = name
#         self.age = age
#         self.coat = coat
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# buddy = Dog("Buddy", 9, "white")
# miles = Dog("Miles", 4, "black")
# philo =Dog("Philo", 5, "brown")
# print(miles)
# print(miles.speak("Woof Woof"))
# print(f"{philo.name}, coat is {philo.coat}")

# ex2,ex3

# class Car:
#
#     def __init__(self,color,mileage):
#         self.color= color
#         self.mileage = mileage
#
#     def __str__(self):
#         return f"The {self.color} car has {int(self.mileage)} miles"
#
#     def drive(self,miles):
#         self.mileage = self.mileage + miles
#
# blue_car = Car("Blue",20_000)
# red_car = Car("Red",30_000)
# blue_car.drive(100)
# print(blue_car)
# print(red_car)


# 10.3 INHERIT FROM OTHER CLASSES

#
# class Dog:
#
#     species = "Canis familiars"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} barks: {sound}"
#
# class JackRusselTerrier(Dog):
#     def speak(self,sound ="Arf"):
#         return super().speak(sound)
# class Daschund(Dog):
#     pass
# class Bulldog(Dog):
#     pass
#
# miles = JackRusselTerrier("Miles",4)
# buddy = Daschund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)
#
# print(miles.species)
# print(buddy.name)
# print(jack)
# print(jim.speak("Kurwa jestem psem"))
# print(type(miles))
# print(isinstance(miles,Dog))
# print(isinstance(miles,JackRusselTerrier))
# print(isinstance(miles,Bulldog))
# print(miles.speak())
# print(miles.speak("Grrr"))
#
# print(jim.speak("Woof"))
# print(miles.speak())

#ex1

# class Dog:
#
#     species = "Canis familiars"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} say: {sound}"
#
# class JackRusselTerrier(Dog):
#     def speak(self,sound ="Arf"):
#         return super().speak(sound)
# class Daschund(Dog):
#     pass
# class Bulldog(Dog):
#     pass
# class GoldenRetriver(Dog):
#     def speak(self,sound="Bark"):
#         return super().speak(sound)
#
# golden=GoldenRetriver("Andrzej",5)
# print(golden.speak())


# ex2
#
# class Rectangle:
#
#     def __init__(self,length,width):
#         self.length = float(length)
#         self.width = float(width)
#
#     def area(self):
#         return (self.length * self.width)
#
# class Square(Rectangle):
#     def __init__(self,side_length):
#         super().__init__(side_length, side_length)
#
# square = Square(4)
# print(square.area())
# rectangle= Rectangle(4,85)
# print(rectangle.area())


