from random import sample, randrange
from typing import Tuple, List
import numpy as np

from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, Children, Population, SelectionType, \
    MutationType
from src.utils.cost_function import calculate_cost


class SolveWithEvolutionaryAlgorithm:
    def __init__(self, children: Children, parameters: EvolutionaryAlgorithmParameters):
        self.children = children
        self.parameters = parameters

    def evaluate_algorithm(self) -> Tuple[Children, float]:
        population = [self.children[:] for _ in range(self.parameters.population_number)]
        for _ in range(self.parameters.generations):
            population = self.evaluate_generation(population)

        best = self.select_the_fittest(population, 1)[0]
        return best, calculate_cost(best)

    def evaluate_generation(self, population: Population):
        children = self.breed(copy_list_of_list(population))
        return self.select_the_fittest(population + children, self.parameters.population_number)

    def breed(
            self,
            population: Population,
    ) -> Population:
        parents_to_crossover, else_chromosomes = list_splitter(
            sample(population, len(population)), self.parameters.crossover_probability
        )
        children = []
        for i in range(len(parents_to_crossover) // 2):
            parent_1 = self.select_parent(parents_to_crossover)
            parent_2 = self.select_parent(parents_to_crossover)
            child_1, child_2 = self.crossover(parent_1, parent_2)
            children.append(child_1)
            children.append(child_2)

        a = [self.mutate(chromosome) for chromosome in children + else_chromosomes]
        return a

    @staticmethod
    def crossover(
            parent_1: Children,
            parent_2: Children
    ) -> Tuple[Children, Children]:
        random_index = randrange(0, len(parent_1))
        return parent_1[:random_index] + parent_2[random_index:], parent_2[:random_index] + parent_1[random_index:]

    def mutate(
            self,
            children: Children
    ) -> Children:
        random_index = randrange(0, len(children))
        if children[random_index].cookies == 0:
            return children

        if self.parameters.mutation_type == MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD:
            max_cookies = max([child.cookies for child in children])
            n = randrange(0, max_cookies + 1)
            children[random_index] = children[random_index].take_cookies_immutable(n)
        else:
            children[random_index] = children[random_index].take_cookie_immutable()
        return children

    def select_parent(self, population: Population) -> Children:
        selection_type = self.parameters.selection_type
        if selection_type == SelectionType.ROULETTE:
            return self.roulette_wheel_selection(population)
        elif selection_type == SelectionType.TOURNAMENT:
            return self.tournament_selection(population)
        else:
            return self.tournament_selection(population)

    @staticmethod
    def roulette_wheel_selection(population: Population):
        population_fitness = sum([calculate_cost(chromosome) for chromosome in population])
        chromosome_probabilities = [calculate_cost(chromosome) / population_fitness for chromosome in population]

        chosen_index = np.random.choice(list(range(len(population))), p=chromosome_probabilities)
        return population[chosen_index]

    @staticmethod
    def tournament_selection(population: Population, k: int = 5):
        size_of_bracket = min(len(population), k)
        chosen_to_tournament = sample(population, size_of_bracket)
        best = chosen_to_tournament[0]
        for i in range(1, size_of_bracket):
            if calculate_cost(population[i]) > calculate_cost(best):
                best = population[i]
        return best

    @staticmethod
    def select_the_fittest(
            population: Population,
            select_number
    ) -> Population:
        results = [(individual, calculate_cost(individual)) for individual in population]
        results = sorted(results, key=lambda x: x[1])
        new_population = [individual for (individual, cost) in results]
        return new_population[0:select_number]


def copy_list_of_list(list_to_copy: List[Children]):
    return [inner_list[:] for inner_list in list_to_copy]


def list_splitter(list_to_split, ratio):
    elements = len(list_to_split)
    middle = int(elements * ratio)
    return [list_to_split[:middle], list_to_split[middle:]]
