#import required libraries
import plotly.io as pio
import math
import time
import random

#import custom minecraft libraries
import minecraft.animals as animals
import minecraft.base as base

writeToFile = True
fileName = "outfile_20percent"

gamerules = {
    'entityCramming': 32
}

cowHandler = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)

if writeToFile == True:
    outfile = open('./' + fileName + '.txt', '+w')
    outfile.write("iteration,popsize,leather,beef,experience,playerkills,envdeaths\n")


for i in range(50):
    cowHandler.breed()
    cowHandler.kill(math.floor(cowHandler.population.size*0.2), True, 3)
    if writeToFile == True:
        lootpool = cowHandler.lootpool.returnloot()
        outfile.write(str(i) + ',' + str(cowHandler.population.size) + ',' + str(lootpool["leather"]) + ',' + str(lootpool["beef"]) + ',' + str(lootpool["experience"]) + ',' + str(cowHandler.playerkills) + ',' + str(cowHandler.envdeaths) + '\n')

outfile.close()