#import required libraries
import plotly.io as pio
import math
import time
import random

#import custom minecraft libraries
import minecraft.animals as animals
import minecraft.base as base
import minecraft.agentlib as agentlib

gamerules = {
    'entityCramming': 32
}

# cowHandler00percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)
# cowHandler10percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)
# cowHandler20percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)
# cowHandler30percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)
# cowHandler40percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)
# cowHandler45percent = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 5)

# for i in range(20):
#     cowHandler00percent.breed()
#     cowHandler00percent.killPercent(0, True, 3)
#     cowHandler10percent.breed()
#     cowHandler10percent.killPercent(10, True, 3)
#     cowHandler20percent.breed()
#     cowHandler20percent.killPercent(20, True, 3)
#     cowHandler30percent.breed()
#     cowHandler30percent.killPercent(30, True, 3)
#     cowHandler40percent.breed()
#     cowHandler40percent.killPercent(40, True, 3)
#     cowHandler45percent.breed()
#     cowHandler45percent.killPercent(45, True, 3)

# print("00%: ", cowHandler00percent.lootpool.returnloot())
# print("10%: ", cowHandler10percent.lootpool.returnloot())
# print("20%: ", cowHandler20percent.lootpool.returnloot())
# print("30%: ", cowHandler30percent.lootpool.returnloot())
# print("40%: ", cowHandler40percent.lootpool.returnloot())
# print("45%: ", cowHandler45percent.lootpool.returnloot())

#set up agents and creaturehandlers
chandlers = {}
agents = {}

#make 100
for i in range(100):
    ident = 'a' + str(i)
    agents[ident] = agentlib.agent_test(ident)
    chandlers[ident] = base.animalhandler(animals.cow_base, base.lootpool, 2, gamerules, base.pen_base, 6, 6)

agenthandler = agentlib.agent_handler(agents, chandlers)

for i in range(10):
    agenthandler.doIter(i)

print(agenthandler.fitnesses)