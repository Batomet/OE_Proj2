from Selections import best_select, roulette_select, tournament_select

class SelectionService:
    def __init__(self, individuals, selection_percent, selection_method, maximalization, selected_function):
        self.individuals = individuals
        self.selection_percent = selection_percent
        self.selection_method = selection_method
        self.maximalization = maximalization
        self.selected_function = selected_function

    def select(self):
        if self.selection_method == "BEST":
            return best_select(self.individuals, self.selection_percent, self.maximalization, self.selected_function)
        elif self.selection_method == "ROULETTE":
            return roulette_select(self.individuals, self.selection_percent, self.maximalization, self.selected_function)
        elif self.selection_method == "TOURNAMENT":
            return tournament_select(self.individuals, self.selection_percent, self.maximalization, self.selected_function)
        else:
            raise ValueError("Invalid selection method")