import numpy as np
from data import CROSS


def get_point(begin, end):
    if begin >= end:
        raise ValueError(f"Invalid range for get_point: begin={begin}, end={end}")
    return np.random.randint(low=begin, high=end)


def one_point(individuals, probability):
    individuals_cross = []
    i=0
    while len(individuals_cross) < len(individuals):
        if np.random.random_sample() <= probability:
            random_individuals = get_random_individuals(individuals)

            alpha = np.random.uniform(0, 1)

            chromosome_11 = alpha * random_individuals[0][0] + (1 - alpha) * random_individuals[1][0]
            chromosome_12 = (1 - alpha) * random_individuals[0][0] + alpha * random_individuals[1][0]
            chromosome_21 = alpha * random_individuals[0][1] + (1 - alpha) * random_individuals[1][1]
            chromosome_22 = (1 - alpha) * random_individuals[0][1] + alpha * random_individuals[1][1]

            individuals_cross.append((chromosome_11, chromosome_21))
            individuals_cross.append((chromosome_12, chromosome_22))

    return individuals_cross



def two_point(individuals, probability):
    individuals_cross = []

    while len(individuals_cross) < len(individuals):
        if np.random.random_sample() <= probability:
            random_individuals = get_random_individuals(individuals)

            alpha1, alpha2 = sorted(np.random.uniform(0, 1, 2))

            chromosome_11 = alpha1 * random_individuals[0][0] + (1 - alpha1) * random_individuals[1][0]
            chromosome_12 = alpha2 * random_individuals[0][0] + (1 - alpha2) * random_individuals[1][0]
            chromosome_21 = alpha1 * random_individuals[0][1] + (1 - alpha1) * random_individuals[1][1]
            chromosome_22 = alpha2 * random_individuals[0][1] + (1 - alpha2) * random_individuals[1][1]

            individuals_cross.append((chromosome_11, chromosome_21))
            individuals_cross.append((chromosome_12, chromosome_22))

    return individuals_cross


def grain(individuals, probability, grain_size=2):
    individuals_cross = []

    while len(individuals_cross) < len(individuals):
        if np.random.random_sample() <= probability:
            random_individuals = get_random_individuals(individuals)
            chromosome11, chromosome12 = [], []
            chromosome21, chromosome22 = [], []

            # Alternate grains between parents
            for i in range(0, len(random_individuals[0][0]), grain_size):
                if (i // grain_size) % 2 == 0:
                    chromosome11 += random_individuals[0][0][i:i + grain_size]
                    chromosome12 += random_individuals[0][1][i:i + grain_size]
                    chromosome21 += random_individuals[1][0][i:i + grain_size]
                    chromosome22 += random_individuals[1][1][i:i + grain_size]
                else:
                    chromosome11 += random_individuals[0][1][i:i + grain_size]
                    chromosome12 += random_individuals[0][0][i:i + grain_size]
                    chromosome21 += random_individuals[1][1][i:i + grain_size]
                    chromosome22 += random_individuals[1][0][i:i + grain_size]

            individuals_cross.append((chromosome11, chromosome21))
            individuals_cross.append((chromosome12, chromosome22))

    return individuals_cross

def uniform(individuals, probability):
    individuals_cross = []

    while len(individuals_cross) < len(individuals):
        if np.random.random_sample() <= probability:
            random_individuals = get_random_individuals(individuals)
            chromosome11, chromosome12 = [], []
            chromosome21, chromosome22 = [], []

            mask = np.random.randint(0, 2, len(random_individuals[0][0]))

            for i in range(len(mask)):
                if mask[i] == 0:
                    chromosome11.append(random_individuals[0][0][i])
                    chromosome12.append(random_individuals[0][1][i])
                    chromosome21.append(random_individuals[1][0][i])
                    chromosome22.append(random_individuals[1][1][i])
                else:
                    chromosome11.append(random_individuals[0][1][i])
                    chromosome12.append(random_individuals[0][0][i])
                    chromosome21.append(random_individuals[1][1][i])
                    chromosome22.append(random_individuals[1][0][i])

            individuals_cross.append((chromosome11, chromosome21))
            individuals_cross.append((chromosome12, chromosome22))

    return individuals_cross


def get_random_individuals(individuals):
    length = len(individuals)
    rand_index1 = get_point(0, length)
    rand_index2 = get_point(0, length)

    parent1 = individuals[rand_index1]
    parent2 = individuals[rand_index2]

    return [parent1, parent2]

class CrossoverService:

    def __init__(self, individuals, method, probability):
        self.method = method
        self.individuals = individuals
        self.probability = probability

    def cross(self):
        if self.method == CROSS[0]:
            return one_point(self.individuals, self.probability)
        if self.method == CROSS[1]:
            return two_point(self.individuals, self.probability)
        if self.method == CROSS[2]:
            return grain(self.individuals, self.probability)
        if self.method == CROSS[3]:
            return uniform(self.individuals, self.probability)