import random
from individual import Individual
from population import Population

class SimpleDemoGA:
    def __init__(self, numberOfIndividuals, numberOfGenes):
        self.numberOfGenes = numberOfGenes
        self.population = Population(numberOfIndividuals, numberOfGenes)
        self.generationCount = 0

    def crossover(self):
        # Swap values up to crossoverIndex between fittest and secondFittest
        # This creates a child genome that has a combination of genes from the parents
        # It is not a completely random selection, this function treats each bit as a gene in a sequence
        crossoverIndex = random.randrange(self.numberOfGenes)
        offspring = Individual(self.numberOfGenes)
        tempOffspringGenes = self.population.fittest.genes[0:crossoverIndex]
        for i in range(crossoverIndex,self.numberOfGenes):
            tempOffspringGenes.append(self.population.secondFittest.genes[i])
        # ENHANCEMENT: Add a function to Individual to make a new Individual with specific genes
        # rather than create a new random one and set the genes
        offspring.genes = tempOffspringGenes
        return offspring

    
    def mutation(self, offspring):
        mutationIndex = random.randrange(self.numberOfGenes)
        # Bitflip the mutated index using XOR
        offspring.genes[mutationIndex] ^= 1
    
    # def getFittestOffspring(self):
    #     return self.offspring

    def addFittestOffspring(self, offspring):
        self.population.removeLeastFit()
        self.population.addToPopulation(offspring)
    
    def showGeneticPool(self):
        print("==Genetic Pool==")
        for individual in self.population.individuals:
            print("Individual: {0} Fit: {1} {2}".format(self.population.individuals.index(individual),individual.fitness,individual.genes))
        print("================")


# Main

def main():
    # Parameters for population
    ## Number of individuals per population
    numberOfIndividuals = 10
    ## Number of genes per individual
    numberOfGenes = 10
    ## Set verbose to True to print each genetic pool to the console
    verbose = True
    ## Set generation breakpoint. Set limitGenerations to True to break after maxGenerations has been hit.
    limitGenerations = True
    maxGenerations = 300
    ## Set mutation rate, 0-100 out of 100
    mutationRate = 20
    ## Initial setting to pause after each generation
    pauseGenerations = 'y'

    # Initialize population in this demo object
    demo = SimpleDemoGA(numberOfIndividuals, numberOfGenes)
    # Restart trivial populations, i.e. ones that have a solution before crossover
    while demo.population.fittestScore == demo.numberOfGenes:
        demo = SimpleDemoGA(numberOfIndividuals, numberOfGenes)

    print("Initial population of {0} individuals.".format(demo.population.popSize))
    demo.showGeneticPool()

    # Main loop for genetic algorithm process
    while demo.population.fittestScore < numberOfGenes:
        demo.generationCount += 1
        # Selection occurs naturally
        # demo.selection()
        # Crossover - merge fittest' and secondFittest's genes
        fittestOffspring = demo.crossover()
        # Mutation - random chance
        # Mutate if random number mod 7 is less than 5
        mutationTrigger = random.randrange(100)
        if mutationTrigger <= mutationRate:
            demo.mutation(fittestOffspring)
        # Remove least fit individual, replace with offspring of fittest and secondFittest
        demo.addFittestOffspring(fittestOffspring)
        print("\nGeneration: {0} Fittest Score (out of {1}): {2}".format(demo.generationCount,demo.numberOfGenes,demo.population.fittestScore))
        if mutationTrigger <= mutationRate:
            print("~~~~~~~~~ MUTANT ~~~~~~~~~\nMutation Trigger: {0}".format(mutationTrigger))
        print("Fittest Parents {0}\t{1}".format(demo.population.fittest.genes,demo.population.secondFittest.genes))
        print("Their beautiful child {0}\n".format(fittestOffspring.genes))
        # If verbose is set, print entire generation
        if verbose:
            demo.showGeneticPool()
        if pauseGenerations == 'y':
            print("Pause at next generation? [Y/n]")
            pauseGenerations = input() or 'y'
        if limitGenerations and demo.generationCount >= maxGenerations:
            break
    # End main loop
    
    if demo.population.fittestScore < demo.numberOfGenes:
        # Solution not found
        print("\nSolution NOT found by generation {0}".format(demo.generationCount))
        print("Hint: Try more mutations, or increase the generation count.")
    else:
        # Solution found, give 'victory screen'
        print("\nSolution found in generation {0}! Congratulations!".format(demo.generationCount))
    print("Fitness: {0}".format(demo.population.fittestScore))
    print("Genes: {0}".format(demo.population.fittest.genes))

if __name__ == "__main__":
    main()
