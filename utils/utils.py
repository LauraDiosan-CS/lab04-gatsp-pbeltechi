from random import randint
import math

def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)

def computeDistance(chromosomeRepres,problParamter):
    fitness = 0
    for i in range(len(chromosomeRepres)-1):
        fitness += problParamter['graph'][chromosomeRepres[i]][chromosomeRepres[i+1]]
    fitness += problParamter['graph'][chromosomeRepres[-1]][chromosomeRepres[0]]
    return fitness

def euclideanDistance(x,y):
    # return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)