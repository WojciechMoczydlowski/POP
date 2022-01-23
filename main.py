from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters
from src.generator.generate_date import generate_data

seed = 100
amount = 3

data = generate_data(seed, amount)
print(data)
print(SolveWithEvolutionaryAlgorithm(data, EvolutionaryAlgorithmParameters(population_number=amount)).evaluate_algorithm())
