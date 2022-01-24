from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.generator.generate_date import generate_data
from src.greedy_algorithm.greedy_algorithm import greedy_algorithm

seed = 150
amount = 15

data = generate_data(seed, amount)
print(SolveWithEvolutionaryAlgorithm(data, EvolutionaryAlgorithmParameters(
    population_number=amount,
    generations=100,
    crossover_probability=0.1,
    selection_type=SelectionType.TOURNAMENT,
    mutation_type=MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD
)).evaluate_algorithm())
print(greedy_algorithm(data, 1000))
