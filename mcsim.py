#import required libraries
import plotly.io as pio
from tqdm import tqdm
import math
import time
import random

#import custom minecraft libraries
import minecraft.animals as animals
import minecraft.base as base

#setup classes
#animals
cow = animals.cow_base
pig = animals.pig_base

#lootpools
cow_lootpool = base.lootpool(cow.setup_lootpool())
pig_lootpool = base.lootpool(pig.setup_lootpool())

#populations
cow_population = base.population(2)
pig_population = base.population(2)

for iteration in tqdm(range(30), desc="Simulating breeding iterations"):
    prevsize_cows = cow_population.size
    cow_population.breed()
    size_diff_cows = cow_population.size - prevsize_cows
    for c in range(size_diff_cows):
        cow_lootpool.addloot(cow.breed())
    to_kill_amount_cows = math.floor(cow_population.size * 0.1)
    cow_population.kill(to_kill_amount_cows)
    for ck in range(to_kill_amount_cows):
        cow_lootpool.addloot(cow.kill(True, 0))

    prevsize_pigs = pig_population.size
    pig_population.breed()
    size_diff_pigs = pig_population.size - prevsize_pigs
    for p in range(size_diff_pigs):
        pig_lootpool.addloot(pig.breed())
    to_kill_amount_pigs = math.floor(pig_population.size*0.1)
    pig_population.kill(to_kill_amount_pigs)
    for pk in range(to_kill_amount_pigs):
        pig_lootpool.addloot(pig.kill(True, 0))

print("Cow loot:")
print(cow_lootpool.returnloot())
print("Cows remaining:")
print(cow_population.size)

print("Pig loot:")
print(pig_lootpool.returnloot())
print("Pigs remaining:")
print(pig_population.size)