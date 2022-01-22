from src.evolutionary_algorithm.evolutionary_algorithm import solve_with_evolutionary_algorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters
from src.generator.generate_date import generate_data

seed = 100
amount = 100

data = generate_data(seed, amount)
print(solve_with_evolutionary_algorithm(data, EvolutionaryAlgorithmParameters()))
