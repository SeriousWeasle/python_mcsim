#import required libraries
import plotly.io as pio
import math
import time
import random

#import custom minecraft libraries
import minecraft.animals as animals
import minecraft.base as base

gamerules = {
    'entityCramming': 32
}

cowHandler = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)

for i in range(20):
    cowHandler.breed()
    cowHandler.kill(math.floor(cowHandler.population.size*0.1), True, 0)
    print(cowHandler.lootpool.returnloot())