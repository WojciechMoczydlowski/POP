from dataclasses import dataclass
from enum import Enum, auto
from typing import List

from src.utils.models import Children

Population = List[Children]


class SelectionType(Enum):
    TOURNAMENT = auto()
    ROULETTE = auto()


class MutationType(Enum):
    TAKE_1_CAKE_FROM_RANDOM_CHILD = auto()
    TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD = auto()


@dataclass
class EvolutionaryAlgorithmParameters:
    generations: int = 1000
    population_number: int = 50
    crossover_probability: float = 0.2
    selection_type: SelectionType = SelectionType.ROULETTE
    mutation_type: MutationType = MutationType.TAKE_1_CAKE_FROM_RANDOM_CHILD
