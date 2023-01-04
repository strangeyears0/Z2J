#Class Village
class Village:


    #initialization

    def __init__(self,name,population):
        self.name = name
        self.population = population
    def __str__(self):
        return f"Village name: {self.name}" \
               f"\nPopulation : {self.population}"

    def add_population(self):
        self.population += 1

#Class Townsfolk
class TownsFolk(Village):



    def __init__(self,name,age,race):
        self.name = name
        self.age = age
        self.race = race


    def singing(self, sing = None):
        if sing is None:
            return f"{self.name}'Dont know any song :( "
        return f"{self.name} is singing : \n {sing}"

class Santa(TownsFolk):
    def __str__(self):
        return f"My name is {self.name}, i am {self.age} years old and i was a {self.race}"


class ElfWorker(TownsFolk):

    #clas atribute
    strength = 10
    intelligence = 1

    def __str__(self):
        return f"My name is {self.name}, i am {self.age} years old and i was a {self.race}"

    def singing(self, sing = "Hard Life Worker, Fuck Santa "):
        return super().singing(sing)

    def crafting(self):
        if self.strength > self.intelligence:
            return f"{self.race} craft Rock\n" \
                   f"{self.race} is powerful not smart."

class ElfScientist(TownsFolk):

    strength = 1
    intelligence = 10

    def __str__(self):
        return f"My name is {self.name}, i am {self.age} years old and i was a {self.race}"

    def singing(self, sing = " I love science I love Nuke I love Santa I love Booom"):
        return super().singing(sing)

    def crafting(self):
        if self.strength > self.intelligence:
            return f"{self.race} craft Rock\n" \
                   f"{self.race} is powerful not smart."
        else:
            return f"{self.race} craft NUKE BOMB"

class Building:

    def __init__(self, name, type):
        self.name = name
        self.type = type
    def __str__(self):
        return f"This building is {self.name}, and this is {self.type}"

class Whorehouse(Building):
    def __init__(self, name, type, whore):
        super().__init__(name,type)
        self.whore = whore


    def check_who_is_in_building():


        print( f"Door is open, you see  {santa.name} with {whorehouse.whore}" )





village = Village("Santa Claus City",0)
print(village)
santa = Santa("Santa Claus",100,"Human")
print(santa)
elfworker = ElfWorker("John",9,"Elf Worker")
print(elfworker)
print(elfworker.singing())
print(elfworker.crafting())
elfscientist = ElfScientist("Andrzej",7,"Elf Scientist")
print(elfscientist)
print(elfscientist.singing())
print(elfscientist.crafting())
print(santa.singing())


whorehouse = Whorehouse("Candy Drop","Whorehouse","Lizzy")
print(whorehouse)
Whorehouse.check_who_is_in_building()