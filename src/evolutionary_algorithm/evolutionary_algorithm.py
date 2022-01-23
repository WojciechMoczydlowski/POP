from typing import Tuple
from tqdm import trange

from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, Children, Population
from src.utils.cost_function import calculate_cost


class SolveWithEvolutionaryAlgorithm:
    def __init__(self, children: Children, parameters: EvolutionaryAlgorithmParameters):
        self.children = children
        self.parameters = parameters

    def evaluate_algorithm(self) -> Tuple[Children, float]:
        """
        :param children: Children list
        :param parameters: Parameters
        :return: Optimized children list and cost function
        """
        population = [self.children[:] for i in range(self.parameters.population_number)]
        for i in trange(self.parameters.generations):
            population = self.evaluate_generation(population)

        best = self.select_the_fittest(population, 1)[0]
        return best, calculate_cost(best)

    def evaluate_generation(self, population: Population):
        parents = self.select_the_fittest_to_reproduction(population)
        children = self.breed(parents)
        return self.select_the_fittest(population + children, self.parameters.population_number)

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

    @staticmethod
    def select_the_fittest(
            population: Population,
            select_number
    ) -> Population:
        results = [(individual, calculate_cost(individual)) for individual in population]
        results = sorted(results, key=lambda x: x[1])
        new_population = [individual for (individual, cost) in results]
        return new_population[0:select_number]
