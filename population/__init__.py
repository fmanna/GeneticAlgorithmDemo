from individual import Individual

class Population:
    def __init__(self, popSize, geneLength):
        self.popSize = popSize
        self.geneLength = geneLength
        self.fittestScore = 0
        self.individuals = []
        for i in range(popSize):
            self.individuals.append(Individual(self.geneLength))

    def selectFittest(self):
        maxFit = 0
        maxFitIndex = 0
        for individual in self.individuals:
            individual.setFitness(individual.calcFitness())
            if individual.getFitness() > maxFit:
                maxFit = individual.getFitness()
                maxFitIndex = self.individuals.index(individual)
        self.fittestScore = maxFit
        try:
            cloneOfFittest = Individual(self.geneLength)
            cloneOfFittest.setGenes(self.individuals[maxFitIndex].getGenes())
            cloneOfFittest.setFitness(self.individuals[maxFitIndex].getFitness())
            return cloneOfFittest
        except:
            print("Could not clone individual in index " + maxFitIndex)

    def selectFittestPair(self):
        maxFit1 = 0
        maxFit2 = 0
        maxFitIndex1 = 0
        maxFitIndex2 = 1
        for individual in self.individuals:
            if individual.getFitness() > maxFit1:
                maxFit1 = individual.getFitness()
                maxFitIndex1 = self.individuals.index(individual)
            elif individual.getFitness() > maxFit2:
                maxFit2 = individual.getFitness()
                maxFitIndex2 = self.individuals.index(individual)
        self.fittestScore = maxFit1
        try:
            cloneOfFittest1 = Individual(self.geneLength)
            cloneOfFittest1.setGenes(self.individuals[maxFitIndex1].getGenes())
            cloneOfFittest1.setFitness(self.individuals[maxFitIndex1].getFitness())
            cloneOfFittest2 = Individual(self.geneLength)
            cloneOfFittest2.setGenes(self.individuals[maxFitIndex2].getGenes())
            cloneOfFittest2.setFitness(self.individuals[maxFitIndex2].getFitness())
            return cloneOfFittest1, cloneOfFittest2
        except:
            print("Could not clone fittest pairof indexes " + maxFitIndex1 + " " + maxFitIndex2)
    
    def getPopSize(self):
        return self.popSize

    def getIndividuals(self):
        return self.individuals
    
    def getGeneLength(self):
        return self.geneLength
    
    def getFittestScore(self):
        return self.fittestScore
    
    def getLeastFitIndex(self):
        minFitVal = self.geneLength + 1
        minFitIndex = 0
        for i in range(self.geneLength):
            if minFitVal > self.individuals[i].getFitness():
                minFitVal = self.individuals[i].getFitness()
                minFitIndex = i
        return minFitIndex
    
    def setPopSize(self, newPopSize):
        self.popSize = newPopSize
    
    def setGeneLength(self, newGeneLength):
        self.geneLength = newGeneLength
    
    def setFittestScore(self, newFittestScore):
        self.fittestScore = newFittestScore
    
    def setIndividuals(self, newIndividuals):
        self.individuals = newIndividuals
