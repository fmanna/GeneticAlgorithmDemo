from individual import Individual

class Population:
    def __init__(self, popSize, geneLength):
        self.popSize = popSize
        self.geneLength = geneLength
        self.individuals = []
        for i in range(popSize):
            self.individuals.append(Individual(self.geneLength))

    @property
    def fittest(self):
        fittest, _ = self.selectFittestPair()
        return fittest
    @property
    def secondFittest(self):
        _, secondFittest = self.selectFittestPair()
        return secondFittest
    @property
    def fittestScore(self):
        return self.fittest.fitness
    @property
    def leastFit(self):
        return getLeastFit()
    

    def selectFittestPair(self):
        maxFit1 = 0
        maxFit2 = 0
        maxFitIndex1 = 0
        maxFitIndex2 = 1
        for individual in self.individuals:
            if individual.fitness > maxFit1:
                maxFit1 = individual.fitness
                maxFitIndex1 = self.individuals.index(individual)
            elif individual.fitness > maxFit2:
                maxFit2 = individual.fitness
                maxFitIndex2 = self.individuals.index(individual)
        try:
            cloneOfFittest1 = Individual(self.geneLength)
            cloneOfFittest1.genes = self.individuals[maxFitIndex1].genes
            cloneOfFittest2 = Individual(self.geneLength)
            cloneOfFittest2.genes = self.individuals[maxFitIndex2].genes
            return cloneOfFittest1, cloneOfFittest2
        except:
            print("Could not clone fittest pair of indexes {0} {1}".format(maxFitIndex1,maxFitIndex2))

    def getLeastFit(self):
        minFitVal = self.geneLength + 1
        for individual in self.individuals:
            if minFitVal > individual.fitness:
                minFitVal = individual.fitness
                minFitIndividual = individual
        return minFitIndividual
    
    def removeLeastFit(self):
        try:
            minFitVal = self.geneLength + 1
            for individual in self.individuals:
                if minFitVal > individual.fitness:
                    minFitVal = individual.fitness
                    minFitIndividual = individual
            self.individuals.remove(minFitIndividual)
        except:
            print("Could not remove least fit individual")
    
    def addToPopulation(self, newIndividual):
        self.individuals.append(newIndividual)

def individualFitHelper(elem):
    return elem.fitness
