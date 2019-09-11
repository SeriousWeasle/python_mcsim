import math

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
        self.size = self.size + math.floor(self.size/2)
    
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