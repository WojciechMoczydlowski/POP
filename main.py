from src.evolutionary_algorithm.evolutionary_algorithm import solve_with_evolutionary_algorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters
from src.generator.generate_date import generate_data
from src.greedy_algorithm.greedy_algorithm import greedy_algorithm

seed = 150
amount = 10

data = generate_data(seed, amount)
print(solve_with_evolutionary_algorithm(data, EvolutionaryAlgorithmParameters()))
results = greedy_algorithm(data, 1000)
