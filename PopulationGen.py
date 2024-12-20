import numpy as np


def generate_values(amount: int, population_range: list):

    return np.random.uniform(low=population_range[0], high=population_range[1], size=amount)


class PopulationGenerator:

    def __init__(self, amount, population_range):
        self.amount = amount
        self.population_range = population_range

    def generate(self):

        x1 = generate_values(self.amount, self.population_range)
        x2 = generate_values(self.amount, self.population_range)
        population = []
        for item in zip(x1, x2):
            population.append(item)
        return population
