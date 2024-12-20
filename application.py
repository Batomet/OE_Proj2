import tkinter as tk
import numpy as np
import time
from tkinter import ttk
from tkinter import messagebox
from data import *
from PlaceHolder import *
from PopulationGen import PopulationGenerator
from ServiceSelection import SelectionService
from ChromosomeConverter import ChromosomeConverter
from CrossoverService import CrossoverService
from MutationService import MutationService
from InversionService import InversionService
from StrategyService import StrategyService
from ChartsService import ChartsService
from Selections import get_selected_function


class Application(tk.Frame):

    def __init__(self, master=None):

        super().__init__(master)
        self.master = master
        self.master.title("Genetic Algorithm")
        self.create_widget()
        self.selected_function = FUNCTION[0]

    def create_widget(self):
        self.title = tk.Label(text="Population Range", font=('Arial', 12, 'bold'))
        self.title.grid(row=0, column=0, columnspan=2, pady=(5, 10))

        self.label_begin_range = tk.Label(text="Begin population range:")
        self.label_begin_range.grid(row=1, column=0, sticky='e', padx=5, pady=3)
        self.begin_range = Placeholder(master=self.master, placeholder=-10, width=20)
        self.begin_range.grid(row=1, column=1, pady=3)

        self.label_end_range = tk.Label(text="End population range:")
        self.label_end_range.grid(row=2, column=0, sticky='e', padx=5, pady=3)
        self.end_range = Placeholder(master=self.master, placeholder=10, width=20)
        self.end_range.grid(row=2, column=1, pady=3)

        # Grupa druga - ustawienia populacji i precyzji
        self.label_population_amount = tk.Label(text="Population size:")
        self.label_population_amount.grid(row=3, column=0, sticky='e', padx=5, pady=3)
        self.population_amount = Placeholder(master=self.master, placeholder=100, width=20)
        self.population_amount.grid(row=3, column=1, pady=3)

        self.label_precision = tk.Label(text="Precision:")
        self.label_precision.grid(row=4, column=0, sticky='e', padx=5, pady=3)
        self.precision = Placeholder(master=self.master, placeholder="4", width=20)
        self.precision.grid(row=4, column=1, pady=3)

        # Grupa trzecia - epoki i metody
        self.label_epochs_amount = tk.Label(text="Epochs amount:")
        self.label_epochs_amount.grid(row=5, column=0, sticky='e', padx=5, pady=3)
        self.epochs_amount = Placeholder(master=self.master, placeholder="70", width=20)
        self.epochs_amount.grid(row=5, column=1, pady=3)

        self.label_function_choice = tk.Label(text="Function:")
        self.label_function_choice.grid(row=6, column=0, sticky='e', padx=5, pady=3)
        self.function_option_menu = ttk.Combobox(values=FUNCTION, width=18)
        self.function_option_menu.current(0)
        self.function_option_menu.grid(row=6, column=1, pady=3)

        self.label_selection_method = tk.Label(text="Selection method:")
        self.label_selection_method.grid(row=7, column=0, sticky='e', padx=5, pady=3)
        self.selection_option_menu = ttk.Combobox(values=SELECTIONS, width=18)
        self.selection_option_menu.current(0)
        self.selection_option_menu.grid(row=7, column=1, pady=3)

        self.label_cross_method = tk.Label(text="Cross method:")
        self.label_cross_method.grid(row=8, column=0, sticky='e', padx=5, pady=3)
        self.cross_option_menu = ttk.Combobox(values=CROSS, width=18)
        self.cross_option_menu.current(0)
        self.cross_option_menu.grid(row=8, column=1, pady=3)

        self.label_mutation_method = tk.Label(text="Mutation method:")
        self.label_mutation_method.grid(row=9, column=0, sticky='e', padx=5, pady=3)
        self.mutation_option_menu = ttk.Combobox(values=MUTATION, width=18)
        self.mutation_option_menu.current(0)
        self.mutation_option_menu.grid(row=9, column=1, pady=3)

        # Grupa czwarta - parametry algorytmu
        self.label_selection_percent = tk.Label(text="Selection percent:")
        self.label_selection_percent.grid(row=10, column=0, sticky='e', padx=5, pady=3)
        self.selection_percent = Placeholder(master=self.master, placeholder="85", width=20)
        self.selection_percent.grid(row=10, column=1, pady=3)

        self.label_strategy_amount = tk.Label(text="Elite strategy amount:")
        self.label_strategy_amount.grid(row=11, column=0, sticky='e', padx=5, pady=3)
        self.strategy_amount = Placeholder(master=self.master, placeholder="20", width=20)
        self.strategy_amount.grid(row=11, column=1, pady=3)

        self.label_cross_probability = tk.Label(text="Cross probability:")
        self.label_cross_probability.grid(row=12, column=0, sticky='e', padx=5, pady=3)
        self.cross_probability = Placeholder(master=self.master, placeholder="0.9", width=20)
        self.cross_probability.grid(row=12, column=1, pady=3)

        self.label_mutation_probability = tk.Label(text="Mutation probability:")
        self.label_mutation_probability.grid(row=13, column=0, sticky='e', padx=5, pady=3)
        self.mutation_probability = Placeholder(master=self.master, placeholder="0.2", width=20)
        self.mutation_probability.grid(row=13, column=1, pady=3)

        self.label_inversion_probability = tk.Label(text="Inversion probability:")
        self.label_inversion_probability.grid(row=14, column=0, sticky='e', padx=5, pady=3)
        self.inversion_probability = Placeholder(master=self.master, placeholder="0.2", width=20)
        self.inversion_probability.grid(row=14, column=1, pady=3)

        # Opcja maksymalizacji
        self.maximization_value = tk.BooleanVar()
        self.maximization_value.set(False)
        self.maximization_check = tk.Checkbutton(text='Maximalization', var=self.maximization_value)
        self.maximization_check.grid(row=15, column=0, columnspan=2, pady=(10, 10))

        # Przycisk startowy
        self.start = tk.Button(text="START", command=self.start, width=20, height=2, bg="green", fg="white",
                               font=('Arial', 10, 'bold'))
        self.start.grid(row=16, column=0, columnspan=2, pady=(5, 10))

    def start(self):
        try:
            input = {
                "begin_range": self.begin_range.value(),
                "end_range": self.end_range.value(),
                "population_amount": self.population_amount.value(),
                "precision": self.precision.value(),
                "epochs_amount": self.epochs_amount.value(),
                "selected_function": self.function_option_menu.get(),
                "selection_percent": self.selection_percent.value(),
                "strategy_amount": self.strategy_amount.value(),
                "cross_probability": float(self.cross_probability.get()),
                "mutation_probability": float(self.mutation_probability.get()),
                "inversion_probability": float(self.inversion_probability.get()),
                "selection_method": self.selection_option_menu.get(),
                "cross_method": self.cross_option_menu.get(),
                "mutation_method": self.mutation_option_menu.get(),
                "maximalization": self.maximization_value.get()

            }

            start = time.time()

            population_generator = PopulationGenerator(input["population_amount"],
                                                       [input["begin_range"], input["end_range"]])
            population = population_generator.generate()

            bests_from_epochs = []
            average_from_epochs = []
            std_from_epochs = []
            x1 = []
            x2 = []

            for i in range(input["epochs_amount"]):
                strategy_service = StrategyService(population, input["strategy_amount"], input["maximalization"], input["selected_function"])
                elite = strategy_service.get_elite()

                selection_service = SelectionService(population,
                                                     input["selection_percent"],
                                                     input["selection_method"],
                                                     input["maximalization"],
                                                     input["selected_function"])
                selected = selection_service.select()

                if len(selected) <= 1:
                    break

                individuals_bin_chromosomes = ChromosomeConverter.to_real(selected,
                                                                             input["begin_range"],
                                                                             input["end_range"],
                                                                             input["precision"])

                crossover_service = CrossoverService(individuals_bin_chromosomes,
                                                     input["cross_method"],
                                                     input["cross_probability"])
                crossed_individuals = crossover_service.cross()

                mutation_service = MutationService(crossed_individuals,
                                                   input["mutation_method"],
                                                   input["mutation_probability"])
                mutated_individuals = mutation_service.mutate()

                inversion_service = InversionService(mutated_individuals,
                                                     input["inversion_probability"])
                inversed_individuals = inversion_service.inverse()

                new_individuals_dec_chromosomes = ChromosomeConverter.to_decimals(inversed_individuals,
                                                                                 input["begin_range"],
                                                                                 input["end_range"],
                                                                                 input["precision"])
                population = elite + new_individuals_dec_chromosomes
                bests_from_epochs.append(
                    (get_selected_function(population[0][0], population[0][1], input["selected_function"])))
                x1.append(population[0][0])
                x2.append(population[0][1])
                fun_result = 0
                stds = []
                for individual in population:
                    levy_result = get_selected_function(individual[0], individual[1], input["selected_function"])
                    fun_result += levy_result
                    stds.append(levy_result)
                average_from_epochs.append(fun_result // len(population))
                std_from_epochs.append(np.std(stds))

            ChartsService.best_chart(bests_from_epochs, x1, x2)
            ChartsService.average_chart(average_from_epochs)
            ChartsService.std_chart(std_from_epochs)

            end = time.time()
            print(end - start)
        except Exception as e:
            print(e)
            tk.messagebox.showinfo("Error", "Incorrect Values")