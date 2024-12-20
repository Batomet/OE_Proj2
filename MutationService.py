import numpy as np
from data import MUTATION

def get_point(begin, end):
    return np.random.randint(low=begin, high=end)


def one_point(individuals, probability):
    counter = 0
    for chromosomes in individuals:
        if np.random.random_sample() <= probability:
            mutation_value1 = np.random.uniform(-1, 1)
            mutation_value2 = np.random.uniform(-1, 1)
            temp_chromosome1 = chromosomes[0] + mutation_value1
            temp_chromosome2 = chromosomes[1] + mutation_value2

            individuals[counter] = (temp_chromosome1, temp_chromosome2)
        counter += 1
    return individuals




def two_point(individuals, probability):
    counter = 0
    for chromosomes in individuals:
        if np.random.random_sample() <= probability:
            mutation_value1 = np.random.uniform(-1, 1)
            mutation_value2 = np.random.uniform(-1, 1)
            mutation_value3 = np.random.uniform(-1, 1)
            mutation_value4 = np.random.uniform(-1, 1)

            temp_chromosome1 = chromosomes[0] + mutation_value1 + mutation_value2
            temp_chromosome2 = chromosomes[1] + mutation_value3 + mutation_value4

            individuals[counter] = (temp_chromosome1, temp_chromosome2)
        counter += 1
    return individuals


def boundary(individuals, probability):
    counter = 0
    for chromosomes in individuals:
        if np.random.random_sample() <= probability:
            mutation_value1 = np.random.uniform(-1, 1)
            mutation_value2 = np.random.uniform(-1, 1)

            boundary_choice1 = np.random.choice(['lower', 'upper'])
            boundary_choice2 = np.random.choice(['lower', 'upper'])

            temp_chromosome1 = chromosomes[0]
            temp_chromosome2 = chromosomes[1]

            if boundary_choice1 == 'lower':
                temp_chromosome1 += mutation_value1
            else:
                temp_chromosome1 -= mutation_value1

            if boundary_choice2 == 'lower':
                temp_chromosome2 += mutation_value2
            else:
                temp_chromosome2 -= mutation_value2

            individuals[counter] = (temp_chromosome1, temp_chromosome2)

        counter += 1
    return individuals




class MutationService:

    def __init__(self, individuals, method, probability):
        self.method = method
        self.individuals = individuals
        self.probability = probability

    def mutate(self):
        if self.method == MUTATION[0]:
            return one_point(self.individuals, self.probability)
        if self.method == MUTATION[1]:
            return two_point(self.individuals, self.probability)
        if self.method == MUTATION[2]:
            return boundary(self.individuals, self.probability)
