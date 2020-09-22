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
        self.offspring = Individual(numberOfGenes)
    
    def selection(self):
        self.fittest, self.secondFittest = self.population.selectFittestPair()

    def crossover(self):
        # Swap values up to crossoverIndex between fittest and secondFittest
        # This creates a child genome that has a combination of genes from the parents
        # It is not a completely random selection, this function treats each bit as a gene in a sequence
        crossoverIndex = random.randrange(self.numberOfGenes)
        #self.offspring.setGenes(self.secondFittest.getGenes())
        tempOffspringGenes = self.secondFittest.getGenes()
        for i in range(crossoverIndex):
            tempOffspringGenes[i] = self.fittest.genes[i]
        self.offspring.setGenes(tempOffspringGenes)   

    
    def mutation(self):
        mutationIndex = random.randrange(self.numberOfGenes)
        # Bitflip the mutated index using XOR
        self.offspring.genes[mutationIndex] ^= 1
        # self.secondFittest.genes[mutationIndex] ^= 1
    
    def getFittestOffspring(self):
        return self.offspring

    def addFittestOffspring(self):
        leastFitIndex = self.population.getLeastFitIndex()
        self.population.individuals[leastFitIndex] = self.getFittestOffspring()
    
    def showGeneticPool(self):
        print("==Genetic Pool==")
        for individual in self.population.individuals:
            print("Individual: {0} Fit: {1} {2}".format(self.population.individuals.index(individual),individual.getFitness(),individual.getGenes()))
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
    ## Set generation breakpoint. Set limitGenerations to True to break after maxGenerations has been hit.
    limitGenerations = True
    maxGenerations = 30

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
        print("\nGeneration: {0} Fittest Score (out of {1}): {2}".format(demo.generationCount,demo.numberOfGenes,demo.population.getFittestScore()))
        print("Mutation Trigger: {0}".format(mutationTrigger))
        print("Fittest Parents {0}\t{1}".format(demo.fittest.getGenes(),demo.secondFittest.getGenes()))
        print("Their beautiful child {0}".format(demo.getFittestOffspring().getGenes()))
        # If verbose is set, print entire generation
        if verbose:
            demo.showGeneticPool()
        if limitGenerations and demo.generationCount >= maxGenerations:
            break
    # End main loop

    # Solution found, give 'victory screen'
    print("\nSolution found in generation {0}".format(demo.generationCount))
    print("Fitness: {0}".format(demo.population.getFittestScore()))
    print("Genes: {0}".format(demo.fittest.getGenes()))

if __name__ == "__main__":
    main()
