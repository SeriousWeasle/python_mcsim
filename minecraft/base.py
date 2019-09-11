import math
import minecraft.animals as animals

class lootpool:
    def __init__(self, loot_dict):
        for item in loot_dict:
            setattr(self, item, 0)
    
    def addloot(self, loot_dict):
        for item in loot_dict:
            setattr(self, item, (getattr(self, item) + loot_dict[item]))
    
    def returnloot(self):
        return self.__dict__

class population:
    def __init__(self, amount):
        self.size = amount
    
    def breed(self):
        new_animals = math.floor(self.size/2)
        self.size = self.size + new_animals
        return new_animals
    
    def setSize(self, newsize):
        self.size(newsize)

    def kill(self, amount):
        if self.size < amount:
            return {"killed": self.size, "remaining": 0}
            self.size = 0
        else:
            prevsize = self.size
            self.size = self.size - amount
            return {"killed": amount, "remaining": self.size}

class animalhandler:
    def __init__(self, creature, lootpool, start_size):
        self.creature = creature
        self.lootpool = lootpool(creature.setup_lootpool())
        self.population = population(start_size)
    
    def kill(self, amount, isPlayerKill, lootingLevel):
        kill_amount = self.population.kill(amount)["killed"]
        for kill in range(kill_amount):
            self.lootpool.addloot(self.creature.kill(isPlayerKill, lootingLevel))
    
    def breed(self):
        newcreatures = self.population.breed()
        for c in range(newcreatures):
            self.lootpool.addloot(self.creature.breed())