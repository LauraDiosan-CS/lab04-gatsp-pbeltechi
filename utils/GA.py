from domain.Chromosome import Chromosome
from random import randint,uniform

class GA:
    def __init__(self, param = None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
    
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for _ in range(0, self.__param["popSize"]):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres,self.__problParam)
            
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (best.fitness > c.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        best = self.__population[0]
        index = 0
        bestIndex = 0
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
                bestIndex = index
            index += 1
        return best,bestIndex
    
    #selection
    def selection2(self):
        pos1 = randint(0, self.__param["popSize"] - 1)
        pos2 = randint(0, self.__param["popSize"] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    #roulette selection        
    def selection(self):
        fitnessSum = 0.0
        for c in self.__population:
            fitnessSum += 1/c.fitness
        sum = uniform(0, fitnessSum)
        partialSum = 0.0
        for i in range(self.__param['noNodes']-1):
            partialSum += self.__population[i].fitness
            if partialSum > sum:
                return i
        return -1
    
    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param["popSize"] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
        
    def oneGenerationSteadyState(self):
        newPop = []
        for _ in range(self.__param["popSize"]):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['function'](off.repres,self.__problParam)
            worst,index = self.worstChromosome()
            if (off.fitness < worst.fitness):
                # self.__population[index] = off
                newPop.append(off)
            else:
                newPop.append(self.__population[index])
        self.__population = newPop
