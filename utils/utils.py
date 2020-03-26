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
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm
