from typing import List, Tuple
import math
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters
from src.utils.child import Child


def solve_with_evolutionary_algorithm(
        children: List[Child], parameters: EvolutionaryAlgorithmParameters
) -> Tuple[List[Child], float]:
    """
    :param children: Children list
    :param parameters: Parameters
    :return: Optimized children list and cost function
    """
    return children, calculate_cost(children)


def calculate_cost(children: List[Child]) -> float:
    if not check_if_configuration_of_children_with_cookies_is_valid(children):
        return math.inf

    return sum([child.cookies for child in children])


def check_if_configuration_of_children_with_cookies_is_valid(children: List[Child]) -> bool:
    """If children sit side by side, a child with higher mark must have more cookies than a child with lower mark."""
    previous_child = Child(0, 0)
    for child in children:
        if previous_child.mark > child.mark and child.cookies > previous_child.cookies:
            return False
        previous_child = child
    return True

