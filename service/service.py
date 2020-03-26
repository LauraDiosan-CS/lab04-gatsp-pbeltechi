from utils.utils import computeDistance
from utils.GA import GA
import matplotlib.pyplot as plt 

class Service:
    def __init__(self,repository):
        self.__repository = repository
        self.__gaParam = {'noNodes': self.__repository.get_noNodes()}
        self.__problParam = {'function' : computeDistance, 'noNodes' : self.__repository.get_noNodes(), 'graph': self.__repository.get_graph()}
    
    def setPopSize(self,size):
        self.__gaParam['popSize']=size
    
    def setGenerationsNumber(self,size):
        self.__gaParam['noGen']=size
        
    def get_repository(self):
        return self.__repository

    """
        creates generations from given population, returns the best chromosome 
    """
    def solveTsp(self,popSize,noGen):
        self.setPopSize(popSize)
        self.setGenerationsNumber(noGen)
        
        #DEBUG
        # self.__repository.writeGraph(self.__problParam['graph'])
        
        ga = GA(self.__gaParam, self.__problParam)
        ga.initialisation()
        ga.evaluation()

        stop = False
        g = -1
        while (not stop and g < self.__gaParam['noGen']):
            g += 1
            # ga.oneGeneration()
            # ga.oneGenerationElitism()
            ga.oneGenerationSteadyState()
            bestChromo = ga.bestChromosome()
            # print(ga.population)
            print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
        self.__repository.writeBest(bestChromo.repres,bestChromo.fitness)
        return bestChromo