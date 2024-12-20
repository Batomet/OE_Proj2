from Selections import best_select


class StrategyService:

    def __init__(self, individuals, strategy_amount, maximalization, selected_function):

        self.individuals = individuals
        self.strategy_amount = strategy_amount
        self.maximalization = maximalization
        self.selected_function = selected_function

    def get_elite(self):

        return best_select(self.individuals, self.strategy_amount, self.maximalization, self.selected_function)
