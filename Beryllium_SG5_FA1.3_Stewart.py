class Hero:

    def __init__(self, name, health):

        self.name = name
        self.health = health

hero1 = Hero("Arthur", 100)
hero2 = Hero("Morgana", 100)

def take_damage(self):

    self.health = self.health - 10
    print(f"{self.name} took 10 damage!")

    print(f"{self.name} has {self.health} health left!")

take_damage(hero1)

print(hero2.name, "is at full health!")