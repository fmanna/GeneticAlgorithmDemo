import random
import sys

sys.path.append('/Users/frank.manna@intersection.com/Documents/GitHub/GeneticAlgorithmDemo/')
from population import Population
from individual import Individual

numberOfGenes = 10
fittest = Individual(numberOfGenes)
secondFittest = Individual(numberOfGenes)


# Swap values up to crossoverIndex between fittest and secondFittest
# This creates a child genome that has a combination of genes from the parents
# It is not a completely random selection, this function treats each bit as a gene in a sequence
crossoverIndex = random.randrange(numberOfGenes)
offspring = Individual(numberOfGenes)
tempOffspringGenes = fittest.genes[0:crossoverIndex]
for i in range(crossoverIndex,numberOfGenes):
    tempOffspringGenes.append(secondFittest.genes[i])
# ENHANCEMENT: Add a function to Individual to make a new Individual with specific genes
# rather than create a new random one and set the genes
offspring.genes = tempOffspringGenes

print("Parent 1:\t{0}".format(fittest.genes))
print("Parent 2:\t{0}".format(secondFittest.genes))
print("\nTheir child:\t{0}".format(offspring.genes))
print("Crossover point: {0}".format(crossoverIndex))

