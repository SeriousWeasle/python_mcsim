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
print("")
print(agenthandler.doGeneration(50))