#import required libraries
import plotly.io as pio
import math
import time
import random

#import custom minecraft libraries
import minecraft.animals as animals
import minecraft.base as base

cowHandler = base.animalhandler(animals.cow_base, base.lootpool, 2)
pigHandler = base.animalhandler(animals.pig_base, base.lootpool, 2)

for i in range(30):
    cowHandler.breed()
    cowHandler.kill(math.floor(cowHandler.population.size*0.10), True, 0)
    pigHandler.breed()
    pigHandler.kill(math.floor(pigHandler.population.size*0.10), True, 0)

print(cowHandler.population.size)
print(cowHandler.lootpool.returnloot())

print(pigHandler.population.size)
print(pigHandler.lootpool.returnloot())