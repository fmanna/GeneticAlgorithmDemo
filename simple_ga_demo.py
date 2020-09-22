import random
from individual import Individual
from population import Population

class SimpleDemoGA:
    def __init__(self, numberOfIndividuals, numberOfGenes):
        self.numberOfGenes = numberOfGenes
        self.population = Population(numberOfIndividuals, numberOfGenes)
        self.generationCount = 0
        # Create dummies for fittest and secondFittest
        self.fittest = Individual(numberOfGenes)
        self.secondFittest = Individual(numberOfGenes)
    
    def selection(self):
        self.fittest, self.secondFittest = self.population.selectFittestPair()

    def crossover(self):
        # Swap values up to crossoverIndex between fittest and secondFittest
        # This creates a child genome that has a combination of genes from the parents
        # It is not a completely random selection, this function treats each bit as a gene in a sequence
        crossoverIndex = random.randrange(self.numberOfGenes)
        for i in range(crossoverIndex):
            fittestGene = self.fittest.genes[i]
            self.fittest.genes[i] = self.secondFittest.genes[i]
            self.secondFittest.genes[i] = fittestGene

    
    def mutation(self):
        mutationIndex = random.randrange(self.numberOfGenes)
        # Bitflip the mutated index using XOR
        self.fittest.genes[mutationIndex] ^= 1
        self.secondFittest.genes[mutationIndex] ^= 1
    
    #def getFittestOffspring(self):

    def addFittestOffspring(self):
        leastFitIndex = self.population.getLeastFitIndex()
        self.population.individuals[leastFitIndex] = self.fittest
    
    def showGeneticPool(self):
        print("==Genetic Pool==")
        for individual in self.population.individuals:
            print("Fit: {0} [{1}]\t{2}".format(individual.getFitness(),individual.getGenes(),bool(sum(individual.getGenes()) == individual.getFitness())))
        print("================")

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

    print("Initial population of {0} individuals.".format(demo.population.popSize))

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
        # Remove least fit individual, replace with offspring of fittest and secondFittest
        demo.addFittestOffspring()
        print("\nGeneration: {0} Fittest Score (out of {1}): {2}".format(demo.generationCount,demo.numberOfGenes,demo.fittest.getFitness()))
        # If verbose is set, print entire generation
        if verbose:
            demo.showGeneticPool()
    # End main loop

    # Solution found, give 'victory screen'
    print("\nSolution found in generation {0}".format(demo.generationCount))
    print("Fitness: {0}".format(demo.population.getFittestScore()))
    print("Genes: {0}".format(demo.fittest.getGenes()))

if __name__ == "__main__":
    main()
