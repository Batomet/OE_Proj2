import numpy as np


class ChromosomeConverter:

    @staticmethod
    def to_real(chromosomes, begin_range, end_range, precision):
        real_representation = []
        for chromosome in chromosomes:
            real_x1 = begin_range + chromosome[0] * (end_range - begin_range) / (10 ** precision)
            real_x2 = begin_range + chromosome[1] * (end_range - begin_range) / (10 ** precision)
            real_representation.append((real_x1, real_x2))
        return real_representation

    @staticmethod
    def to_decimals(chromosomes, begin_range, end_range, precision):
        decimal_representation = []
        for chromosome in chromosomes:
            dec_x1 = int(np.round((chromosome[0] - begin_range) / (end_range - begin_range) * (10 ** precision)))
            dec_x2 = int(np.round((chromosome[1] - begin_range) / (end_range - begin_range) * (10 ** precision)))
            decimal_representation.append((dec_x1, dec_x2))
        return decimal_representation
