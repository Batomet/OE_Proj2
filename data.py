import numpy as np

SELECTIONS = ["BEST", "ROULETTE", "TOURNAMENT"]
CROSS = ["ONE_POINT", "TWO_POINT", "GRAIN", "UNIFORM"]
MUTATION = ["ONE_POINT", "TWO_POINT", "BOUNDARY"]
FUNCTION = ["Martin and Gaddy", "Ackley"]

def martin_and_gaddy(x1, x2):
    return (x1 - x2)**2 + ((x1 + x2 - 10) / 3)**2

def ackley(x1, x2):
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.e
