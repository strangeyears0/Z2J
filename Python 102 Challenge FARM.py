# Challange:FARM

class Animal:

    #Class atributes
    stuff_in_belly = 0
    position = 0

    def __init__(self,name,color):
        self.name = name
        self.color = color

    #instance methods

    def talk(self, sound=None):
        """Return string <name> says <sound>
        if sounds is out return "Hello I'm <name>"""
        if sound is None:
            return f"Hello I'm {self.name}"
        return f"{self.name} says {sound}"

    def walk(self, walk_increment):
        self.position =self.position + walk_increment
        return self.position

    def run(self, run_increment):
        self.position = self.position + run_increment
        return self.position

    def feed(self):
        self.stuff_in_belly = self.stuff_in_belly + 1
        if self.stuff_in_belly >3 :
            return self.poop()
        else:
            return f"{self.name} is eating"

    def is_hungry(self):
        if self.stuff_in_belly < 2:
            return f"{self.name} is hungry"
        else:
            return f"{self.name} is not hungry"

    def poop(self):
        self.stuff_in_belly = 0
        return f"{self.name} is doing Shit"
class Dog(Animal):
    def talk(self, sound = "Bark"):
        return super().talk(sound)

    def fetch(self):
        return f"{self.name} is fetching"

class Sheep(Animal):
    def talk(self, sound = "Meeeee"):
        return super().talk(sound)

class Pig(Animal):
    def talk(self, sound = "Oink"):
        return super().talk(sound)

#HOW IT WORKS:
dog = Dog("Adolf", "white")

print(f"Dog name is {dog.name}")

print(f"And he's {dog.color}")
print(f"Say something {dog.name}")
print(dog.talk())
print("Go Fetch !")
print(dog.fetch())
#dog walk
print(f"{dog.name} is now at position {dog.walk(2)}")
#dog run
print(f"{dog.name} is now at position {dog.run(4)}")

#feed the dog more

print(dog.feed())
print(dog.feed())
print(dog.is_hungry())
print(dog.feed())
print(dog.feed())
print("\n")

#create a sheep

sheep = Sheep("Shaun", "black")
print(f"Sheep is in position {sheep.run(2)}")
print(f"Sheep is in position {sheep.run(2)}")
print(sheep.feed())
print(sheep.feed())
print(sheep.feed())
print(sheep.feed())
print("\n")

#create a pig

pig= Pig("Jew", "pink")

print(pig.talk())
print(pig.is_hungry())
print(pig.is_hungry())
print(pig.is_hungry())
print(pig.is_hungry())
print(pig.is_hungry())