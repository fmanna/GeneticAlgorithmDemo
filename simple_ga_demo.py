import random
from individual import Individual
from population import Population

class SimpleDemoGA:
    def __init__(self, numberOfIndividuals, numberOfGenes):
        self.numberOfGenes = numberOfGenes
        self.population = Population(numberOfIndividuals, numberOfGenes)
        self.generationCount = 0
    
    def selection(self):
        fittest, secondFittest = self.population.selectFittestPair()

    def crossover(self, fittest, secondFittest):
        crossoverIndex = random.randrange(self.numberOfGenes)
        #Swap values at crossoverIndex between fittest and secondFittest
        fittestGene = fittest[crossoverIndex]
        fittest[crossoverIndex] = secondFittest[crossoverIndex]
        secondFittest[crossoverIndex] = fittestGene

    
    def mutation(self, fittest, secondFittest):
        mutationIndex = random.randrange(self.numberOfGenes)
        # Bitflip the mutated index using XOR
        fittest[mutationIndex] ^= 1
        secondFittest[mutationIndex] ^= 1
