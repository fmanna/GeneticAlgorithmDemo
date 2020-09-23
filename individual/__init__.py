import random

class Individual:
    def __init__(self, geneLength):
        # Generate a random array of 1s and 0s
        self.genes = random.choices([0, 1], k=geneLength)
    
    @property
    def geneLength(self):
        return len(self.__genes)
    @property
    def fitness(self):
        return sum(self.__genes)
    @property
    def genes(self):
        return self.__genes
    @genes.setter
    def genes(self, newGenes):
        self.__genes = newGenes

    # Genes will be changed by crossover and mutation
    # def setGenes(self, newGenes):
    #     self.genes = newGenes
    
