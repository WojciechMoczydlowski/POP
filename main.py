import random
from copy import deepcopy
from dataclasses import asdict

from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.generator.generate_date import generate_data
import jsonlines

from src.utils.cost_function import calculate_cost


def save_cookies_numer_and_parameters(init_cookies, final_cookies: float, parameters: EvolutionaryAlgorithmParameters):
    with jsonlines.open('output1.jsonl', mode='a') as writer:
        writer.write({
            'init_cookies': init_cookies,
            'final_cookies': final_cookies,
            'parameters': asdict(parameters)
        })


def main():
    amount = 30
    for i1, generations in enumerate([100, 500, 1000]):
        for i2, seed in enumerate([0, 1, 2]):
            random.seed(seed)
            data = generate_data(amount, 1, 100)
            print(calculate_cost(data))
            for i3, population_number in enumerate([100]):
                for i4, crossover_probability in enumerate([0.3, 0.5, 1]):
                    for i5, selection_type in enumerate([SelectionType.TOURNAMENT, SelectionType.ROULETTE]):
                        for i6, mutation_type in enumerate([MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD]):
                            parameters = EvolutionaryAlgorithmParameters(
                                population_number=population_number,
                                generations=generations,
                                crossover_probability=crossover_probability,
                                selection_type=selection_type,
                                mutation_type=mutation_type
                            )
                            _, total_cookies = SolveWithEvolutionaryAlgorithm(deepcopy(data), parameters).evaluate_algorithm()
                            save_cookies_numer_and_parameters(calculate_cost(data), total_cookies, parameters)
                            print(i1, i2, i3, i4, i5, i6)


main()
