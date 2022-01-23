from typing import Tuple
from tqdm import trange

from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, Children, Population, SelectionType
from src.utils.cost_function import calculate_cost


class SolveWithEvolutionaryAlgorithm:
    def __init__(self, children: Children, parameters: EvolutionaryAlgorithmParameters):
        self.children = children
        self.parameters = parameters

    def evaluate_algorithm(
            self,
            children: Children,
            parameters: EvolutionaryAlgorithmParameters
    ) -> Tuple[Children, float]:
        """
        :param children: Children list
        :param parameters: Parameters
        :return: Optimized children list and cost function
        """
        population = [children[:] for i in range(parameters.population_number)]
        for i in trange(parameters.generations):
            population = self.evaluate_generation(population)

        return children, calculate_cost(children)

    def evaluate_generation(self, population: Population):
        parents = self.select_the_fittest_to_reproduction(population)
        children = self.breed(parents)
        return self.select_the_fittest_to_new_generation(population, children)

    def select_the_fittest_to_reproduction(
            self,
            population: Population
    ) -> Population:
        return population[:]

    def breed(
            self,
            population: Population,
    ) -> Population:
        return population

    def select_the_fittest_to_new_generation(
            self,
            previous_population: Population,
            offspring: Population,
    ) -> Population:
        return previous_population
