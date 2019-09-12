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

class pen_base:
    def __init__(self, width, length, cramming):
        self.width = width
        self.length = length
        self.area = width*length
        self.maxEntities = self.area*cramming

class animalhandler:
    def __init__(self, creature, lootpool, start_size, gamerules, pen, pen_width, pen_length):
        self.creature = creature
        self.lootpool = lootpool(creature.setup_lootpool())
        self.population = population(start_size)
        self.pen = pen(pen_width, pen_length, gamerules["entityCramming"])
        self.playerkills = 0
        self.envdeaths = 0
        self.totaldeaths = {
            "player": 0,
            "environment": 0
        }
        self.breeded = 0
    
    def killPercent(self, percentage, isPlayerKill, lootingLevel):
        percentage = percentage/100
        amount = math.floor(self.population.size*percentage)
        kill_amount = self.population.kill(amount)["killed"]
        self.playerkills = kill_amount
        self.totaldeaths["player"] = self.totaldeaths["player"] + kill_amount
        for kill in range(kill_amount):
            self.lootpool.addloot(self.creature.kill(isPlayerKill, lootingLevel))

    def kill(self, amount, isPlayerKill, lootingLevel):
        kill_amount = self.population.kill(amount)["killed"]
        self.playerkills = kill_amount
        self.totaldeaths["player"] = self.totaldeaths["player"] + kill_amount
        for kill in range(kill_amount):
            self.lootpool.addloot(self.creature.kill(isPlayerKill, lootingLevel))
    
    def breed(self):
        newcreatures = self.population.breed()
        self.breeded = self.breeded + newcreatures
        for c in range(newcreatures):
            self.lootpool.addloot(self.creature.breed())
        if self.population.size > self.pen.maxEntities:
            self.envdeaths = self.population.size - self.pen.maxEntities
            self.totaldeaths["environment"] = self.totaldeaths["environment"] + self.population.size - self.pen.maxEntities
            self.kill(self.population.size - self.pen.maxEntities, False, 0)