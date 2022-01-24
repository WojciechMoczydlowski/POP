from copy import deepcopy
from dataclasses import asdict

from tqdm import tqdm

from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.generator.generate_date import generate_data
from src.greedy_algorithm.greedy_algorithm import greedy_algorithm
import jsonlines


def save_cookies_numer_and_parameters(cookies: float, parameters: EvolutionaryAlgorithmParameters,
                                      greedy_algorithm_cookies: float):
    with jsonlines.open('output.jsonl', mode='a') as writer:
        writer.write({
            'cookies': cookies,
            'parameters': asdict(parameters),
            'greedy_algorithm_cookies': greedy_algorithm_cookies
        })


def main():
    amount = 30
    for i1, seed in enumerate([0, 1, 2]):
        data = generate_data(seed, amount)
        for i2, generations in enumerate([50, 100, 200]):
            for i3, population_number in enumerate([50, 100, 200]):
                for i4, crossover_probability in enumerate([0, 0.1, 0.3]):
                    for i5, selection_type in enumerate([SelectionType.TOURNAMENT, SelectionType.ROULETTE]):
                        for i6, mutation_type in enumerate([MutationType.TAKE_1_CAKE_FROM_RANDOM_CHILD,
                                                            MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD]):
                            parameters = EvolutionaryAlgorithmParameters(
                                population_number=population_number,
                                generations=generations,
                                crossover_probability=crossover_probability,
                                selection_type=selection_type,
                                mutation_type=mutation_type
                            )
                            # _, total_cookies = SolveWithEvolutionaryAlgorithm(deepcopy(data), parameters).evaluate_algorithm()
                            _, greedy_algorithm_cookies = greedy_algorithm(deepcopy(data), 1000)
                            save_cookies_numer_and_parameters(1, parameters, greedy_algorithm_cookies)
                            print(i1, i2, i3, i4, i5, i6)


main()
