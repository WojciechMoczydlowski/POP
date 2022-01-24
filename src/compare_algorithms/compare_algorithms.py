import copy

from src.generator.generate_date import generate_data
from src.greedy_algorithm.greedy_algorithm import greedy_algorithm
from src.evolutionary_algorithm.evolutionary_algorithm import solve_with_evolutionary_algorithm
from src.utils.cost_function import calculate_cost
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters


def compare_algorithms(children_amount, min_mark, max_mark):
    data = generate_data(children_amount, min_mark, max_mark)

    greedy_algorithm_results = greedy_algorithm(copy.deepcopy(data), 50000)
    evolutionary_algorithm_results = solve_with_evolutionary_algorithm(copy.deepcopy(data), EvolutionaryAlgorithmParameters())

    start_cost = calculate_cost(data)
    greedy_algorithm_cost = calculate_cost(greedy_algorithm_results)
    evolutionary_algorithm_cost = calculate_cost(evolutionary_algorithm_results[0])

    return start_cost, greedy_algorithm_cost, evolutionary_algorithm_cost

