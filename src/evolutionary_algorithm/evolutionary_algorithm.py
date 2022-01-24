from typing import List, Tuple
import math
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters
from src.utils.models import Child
from src.utils.cost_function import calculate_cost


def solve_with_evolutionary_algorithm(
        children: List[Child], parameters: EvolutionaryAlgorithmParameters
) -> Tuple[List[Child], float]:
    """
    :param children: Children list
    :param parameters: Parameters
    :return: Optimized children list and cost function
    """
    return children, calculate_cost(children)


