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
        # Swap values up to crossoverIndex between fittest and secondFittest
        # This creates a child genome that has a combination of genes from the parents
        # It is not a completely random selection, this function treats each bit as a gene in a sequence
        crossoverIndex = random.randrange(self.numberOfGenes)
        for i in range(crossoverIndex):
            fittestGene = fittest[i]
            fittest[i] = secondFittest[i]
            secondFittest[i] = fittestGene

    
    def mutation(self, fittest, secondFittest):
        mutationIndex = random.randrange(self.numberOfGenes)
        # Bitflip the mutated index using XOR
        fittest[mutationIndex] ^= 1
        secondFittest[mutationIndex] ^= 1
    
    def getFittestOffspring(self):

    def addFittestOffspring(self):
    
    def showGeneticPool(self):

# Main

def main():
    # Parameters for population
    ## Number of individuals per population
    numberOfIndividuals = 10
    ## Number of genes per individual
    numberOfGenes = 5
    ## Set verbose to True to print each genetic pool to the console
    verbose = True

    # Initialize population in this demo object
    demo = SimpleDemoGA(numberOfIndividuals, numberOfGenes)

    print("Initial population of {0} individuals.".format(demo.popSize))

    # Main loop for genetic algorithm process
    while demo.population.getFittestScore() < numberOfGenes:
        demo.generationCount += 1
        # Selection
        demo.selection()
        # Crossover
        demo.crossover()
        # Mutation - random chance
        # Mutate if random number mod 7 is less than 5
        mutationTrigger = random.randrange(100) % 7
        if mutationTrigger < 5:
            demo.mutation()
    
    # End main loop

if __name__ == "__main__":
    main()
