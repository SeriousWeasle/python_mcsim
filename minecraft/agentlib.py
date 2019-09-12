import random
import operator

class agent_test:
    def __init__(self, identifier):
        self.identifier = identifier

        #inputs to nodes
        self.i1_to_n1 = random.random()
        self.i1_to_n2 = random.random()
        self.i1_to_n3 = random.random()
        self.i2_to_n1 = random.random()
        self.i2_to_n2 = random.random()
        self.i2_to_n3 = random.random()

        #nodes to outputs
        self.n1_to_o1 = random.random()
        self.n1_to_o2 = random.random()
        self.n2_to_o1 = random.random()
        self.n2_to_o2 = random.random()
        self.n3_to_o1 = random.random()
        self.n3_to_o2 = random.random()

        #output factors
        self.killmult = random.random()
        self.breedthreshold = random.randint(0,1000)

    def randomize(self):
        #inputs to nodes
        self.i1_to_n1 = random.random()
        self.i1_to_n2 = random.random()
        self.i1_to_n3 = random.random()
        self.i2_to_n1 = random.random()
        self.i2_to_n2 = random.random()
        self.i2_to_n3 = random.random()

        #nodes to outputs
        self.n1_to_o1 = random.random()
        self.n1_to_o2 = random.random()
        self.n2_to_o1 = random.random()
        self.n2_to_o2 = random.random()
        self.n3_to_o1 = random.random()
        self.n3_to_o2 = random.random()

        #output factors
        self.killmult = random.random()
        self.breedthreshold = random.randint(0,1000)
    
    def in_to_out(self, i1, i2):
        n1 = self.i1_to_n1 * i1 + self.i2_to_n1 * i2
        n2 = self.i1_to_n2 * i1 + self.i2_to_n2 * i2
        n3 = self.i1_to_n3 * i1 + self.i2_to_n3 * i2
        
        o1_calc = self.n1_to_o1 * n1 + self.n2_to_o1 * n2 + self.n3_to_o1 * n3
        o2 = int((self.n1_to_o2 * n1 + self.n2_to_o2 * n2 + self.n3_to_o2 * n3)*self.killmult)

        if(o1_calc > self.breedthreshold):
            o1 = True
        else:
            o1 = False
        return [o1, o2]

class agent_handler:
    def __init__(self, agents, creaturehandlers):
        self.agents = agents
        self.creaturehandlers = creaturehandlers
        self.fitnesses = {}

    def doIter(self, num):
        unsorted_fitnesses = {}
        for a in self.agents:
            ch = self.creaturehandlers[a]
            actions = self.agents[a].in_to_out(self.creaturehandlers[a].population.size, num)
            if actions[0]:
                self.creaturehandlers[a].breed()
            else:
                self.creaturehandlers[a].kill(actions[1], True, 0)
            amountedloot = self.creaturehandlers[a].lootpool.returnloot()
            fitness = self.creaturehandlers[a].population.size + num*0.3 + amountedloot["leather"]*0.2 + amountedloot["beef"]*0.15 + amountedloot["experience"] * 0.25
            unsorted_fitnesses[a] = round(fitness, 1)
        self.fitnesses = sorted(unsorted_fitnesses.items(), key=operator.itemgetter(1))