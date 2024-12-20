from data import martin_and_gaddy, ackley
import numpy as np
from operator import itemgetter
import random

def get_selected_function(x1, x2, selected_function):
    if selected_function == "Martin and Gaddy":
        return martin_and_gaddy(x1, x2)
    elif selected_function == "Ackley":
        return ackley(x1, x2)
    else:
        raise ValueError("Invalid function selection")

def best_select(individuals, selection_percent, maximalization, selected_function):
    function_results_dic = {individual: get_selected_function(individual[0], individual[1], selected_function) for individual in individuals}
    sorted_results = sorted(function_results_dic.items(), key=lambda x: x[1])
    sorted_results = [item[0] for item in sorted_results]

    if maximalization:
        return sorted_results[len(sorted_results) - len(sorted_results) * selection_percent // 100:]

    return sorted_results[:len(sorted_results) * selection_percent // 100]

# Roulette Selection
def roulette_select(individuals, selection_percent, maximalization, selected_function):
    selection_amount = selection_percent // 10

    if maximalization:
        function_results_dic = {individual: get_selected_function(individual[0], individual[1], selected_function) for individual in individuals}
    else:
        function_results_dic = {individual: 1/get_selected_function(individual[0], individual[1], selected_function) for individual in individuals}

    s = 0
    selected = []

    for result in function_results_dic.items():
        s += result[1]

    probabilities = [(key, value/s) for key, value in function_results_dic.items()]
    distributor = 1
    x = []

    for item in probabilities[0:-1]:
        distributor -= item[1]
        tmp_tuple = (item[0], (item[1], distributor))
        x.append(tmp_tuple)

    last_item = (probabilities[len(probabilities) - 1])
    tmp_tuple = (last_item[0], (last_item[1], distributor))
    x.append(tmp_tuple)
    rand_numbers = np.random.rand(selection_amount)

    for i in range(selection_amount):
        closest = get_closest(rand_numbers[i], x)
        if closest != 0.0:
            selected.append(get_closest(rand_numbers[i], x))

    return selected

def get_closest(number, values):
    minimum = values[0][1][1]
    final_value = 0.0

    for val in values:
        diff = abs(val[1][1] - number)
        if diff < minimum:
            final_value = val[0]
            minimum = abs(val[1][1] - number)

    return final_value

# Tournament Selection
def tournament_select(individuals, tournament_size, maximalization, selected_function):
    function_results_dic = {individual: get_selected_function(individual[0], individual[1], selected_function) for individual in individuals}
    function_results_list = list(function_results_dic.items())
    tournaments_winners = []

    if maximalization:
        while len(tournaments_winners) < len(individuals):
            tournament = random.sample(function_results_list, tournament_size)
            winner = max(tournament, key=itemgetter(1))
            tournaments_winners.append(winner[0])
    else:
        while len(tournaments_winners) < len(individuals):
            tournament = random.sample(function_results_list, tournament_size)
            winner = min(tournament, key=itemgetter(1))
            tournaments_winners.append(winner[0])

    return tournaments_winners