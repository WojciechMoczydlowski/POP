import random

from src.compare_algorithms.compare_algorithms import compare_algorithms

seed = 100
random.seed(seed)

results_1 = compare_algorithms(1000, 1, 5)
results_2 = compare_algorithms(1000, 1, 1000)
results_3 = compare_algorithms(100000, 1, 5)
results_4 = compare_algorithms(100000, 1, 1000)
