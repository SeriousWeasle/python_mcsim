import random
class cow_base:
    def setup_lootpool():
        return {
            "leather": 0,
            "beef": 0,
            "experience": 0
        }
    #define loot for killing cows
    def kill(isPlayerKill:bool, lootingLevel):
        #Player kill
        if(isPlayerKill):
            return {
                "leather": random.randint(0,2+lootingLevel),
                "beef": random.randint(1,3+lootingLevel),
                "experience": random.randint(1,3)
            }
        #environmental death
        else:
            return {
                "leather": random.randint(0,2+lootingLevel),
                "beef": random.randint(1,3+lootingLevel)
            }
    #return stuff you get for breeding cows
    def breed():
        return {
            "experience": random.randint(1,7)
        }

class pig_base:
    def setup_lootpool():
        return {
            "porkchop": 0,
            "experience": 0
        }

    def kill(isPlayerKill, lootingLevel):
        if(isPlayerKill):
            return {
            "porkchop": random.randint(1,3+lootingLevel),
            "experience": random.randint(1,3)
        }
        else:
            return {
            "porkchop": random.randint(1,3+lootingLevel)
        }
    
    def breed():
        return {
            "experience": random.randint(1,7)
        }

class chicken_base:
    def setup_lootpool():
        return {
            "chicken": 0,
            "feather": 0,
            "experience": 0
        }

    def kill(isPlayerKill, lootingLevel):
        if(isPlayerKill):
            return {
                "chicken": random.randint(1,1+lootingLevel),
                "feather": random.randint(0,2+lootingLevel),
                "experience": random.randint(1,3)
            }
        else:
            return {
                "chicken": random.randint(1,1+lootingLevel),
                "feather": random.randint(0,2+lootingLevel)
            }
    
    def breed():
        return {
            "experience": random.randint(1,7)
        }


class sheep_base:
    def setup_lootpool():
        return {
            "mutton": 0,
            "wool": 0,
            "experience": 0
        }

    def kill(isPlayerKill, lootingLevel):
        if(isPlayerKill):
            return {
                "mutton": random.randint(1,2+lootingLevel),
                "wool": 1,
                "experience": random.randint(1,3)
            }
        else:
            return {
                "mutton": random.randint(1,2+lootingLevel),
                "wool": 1
            }
    
    def breed():
        return {
            "experience": random.randint(1,7)
        }