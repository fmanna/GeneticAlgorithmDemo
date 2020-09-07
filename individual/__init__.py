import random

class Individual:
    def __init__(self, geneLength):
        self.geneLength = geneLength
        # Generate a random array of 1s and 0s
        self.genes = random.choices([0, 1], k=geneLength)
        self.fitness = sum(self.genes)
    
    def getGeneLength(self):
        return self.geneLength

    def getFitness(self):
        return self.fitness
    
    def getGenes(self):
        return self.genes

    # Certain aberrations can be set to very low fitness, if necessary
    def setFitness(self, newFitness):
        self.fitness = newFitness

    # Genes will be changed by crossover and mutation
    def setGenes(self, newGenes):
        self.genes = newGenes
