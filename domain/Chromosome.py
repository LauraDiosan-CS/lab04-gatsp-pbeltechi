from random import randint,seed
import random
class Chromosome1:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        startNode = self.__problParam['sourceNode']
        self.__nodes = []
        for i in range(0,self.__problParam['noNodes']):
            if i != startNode:
                self.__nodes.append(i)
        self.__repres = random.sample(self.__nodes,self.__problParam['noNodes']-1)
        self.__repres.insert(0,startNode)
        self.__repres.append(startNode)
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        offspring = Chromosome(self.__problParam)
        offspring.__repres = []
        cuttingPoint = randint(0, self.__problParam['noNodes'] - 1)#start and final node are the same
        for i in range(cuttingPoint):
            offspring.__repres.append(self.__repres[i])
        for i in range(0,self.__problParam['noNodes']):
            if c.__repres[i] not in offspring.__repres:
                offspring.__repres.append(c.__repres[i])
        offspring.__repres.append(self.__problParam['sourceNode'])
        return offspring
    
    def mutation(self):
        pos = randint(1, self.__problParam['noNodes'] - 1) #start and final node are the same
        newValue = random.sample(self.__nodes,1)[0]
        for i in range(1,self.__problParam['noNodes']):
            if self.__repres[i] == newValue:
                self.__repres[pos], self.__repres[i] = newValue,self.__repres[pos]
                break

        
    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness


    

def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm

# permutation-based representation
class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam  #problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 
    
    def crossover(self, c):
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1 
        k = 0
        newrepres = self.__repres[pos1 : pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring
    
    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        
    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness