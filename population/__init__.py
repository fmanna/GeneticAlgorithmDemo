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
        fittest, _ = self.selectfittestpair()
        return fittest
    @property
    def secondFittest(self):
        _, secondFittest = self.selectfittestpair()
        return secondFittest
    @property
    def fittestScore(self):
        return self.fittest.getFitness()
    @property
    def leastFit(self):
        return getLeastFit()
    

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
            print("Could not clone fittest pair of indexes " + maxFitIndex1 + " " + maxFitIndex2)
 
    def getLeastFit(self):
        minFitVal = self.geneLength + 1
        for individual in self.individuals:
            if minFitVal > individual.getFitness():
                minFitVal = individual.getFitness()
                minFitIndividual = individual
        return minFitIndividual
    
    def removeLeastFit(self):
        self.individuals.remove(getLeastFit())
    