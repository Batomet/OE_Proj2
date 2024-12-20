import numpy as np

def get_point(begin, end):
    return np.random.uniform(low=begin, high=end)

class InversionService:

    def __init__(self, individuals, probability):
        self.individuals = individuals
        self.probability = probability

    def inverse(self):
        counter = 0

        for chromosomes in self.individuals:
            if np.random.random_sample() <= self.probability:
                mutation_point11 = get_point(min(chromosomes[0], chromosomes[1]), max(chromosomes[0], chromosomes[1]))
                mutation_point12 = get_point(mutation_point11, max(chromosomes[0], chromosomes[1]))

                mutation_point21 = get_point(min(chromosomes[0], chromosomes[1]), max(chromosomes[0], chromosomes[1]))
                mutation_point22 = get_point(mutation_point21, max(chromosomes[0], chromosomes[1]))

                temp_chromosome1 = chromosomes[0]
                temp_chromosome1 = (
                    temp_chromosome1 * (-1) if mutation_point11 < temp_chromosome1 < mutation_point12 else temp_chromosome1
                )

                temp_chromosome2 = chromosomes[1]
                temp_chromosome2 = (
                    temp_chromosome2 * (-1) if mutation_point21 < temp_chromosome2 < mutation_point22 else temp_chromosome2
                )

                self.individuals[counter] = (temp_chromosome1, temp_chromosome2)
            counter += 1

        return self.individuals
