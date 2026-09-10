# Make the class

class Hero:

    # Creation of the class objects

    def __init__(self, name, health):

        self.name = name
        self.health = health

# Birth the heroes into the digital world

hero1 = Hero("Arthur", 100)
hero2 = Hero("Morgana", 100)

# Makes a hero take 10 damage

def take_damage(self):

    self.health = self.health - 10
    print(f"{self.name} took 10 damage!")

    # Show how much health the hero has left

    print(f"{self.name} has {self.health} health left!")

# Makes Arthur take 10 damage and then shows his remaining health

take_damage(hero1)

# Morgana is at full health

print(hero2.name, "is at full health!")