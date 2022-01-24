from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.generator.generate_date import generate_data

seed = 100
amount = 20

data = generate_data(seed, amount)
print(data)
print(SolveWithEvolutionaryAlgorithm(data, EvolutionaryAlgorithmParameters(
    population_number=amount,
    generations=100,
    crossover_probability=0.1,
    selection_type=SelectionType.TOURNAMENT,
    mutation_type=MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD
)).evaluate_algorithm())
