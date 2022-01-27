from src.evolutionary_algorithm.models import MutationType# POP - Evolutionary algorithm for kids with cookies problem

We had to solve the problem:

The teacher wants to give away cookies to children. The children sit in line and each one has some grade (a grade is a natural number). The teacher wants to give at least one cookie to each child. If two kids sit with each other, and one of them has a higher grade than the other, the kid with a higher grade has to get more cookies than the other with a lower grade. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
## Code static analysis
```bash
pytype src
```
## Usage
Run main or:
```python
from src.evolutionary_algorithm.evolutionary_algorithm import SolveWithEvolutionaryAlgorithm
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.generator.generate_date import generate_data

amount = 30
data = generate_data(amount, 1, 100)
parameters = EvolutionaryAlgorithmParameters(
    population_number=100,
    generations=1000,
    crossover_probability=0.1,
    selection_type=SelectionType.TOURNAMENT,
    mutation_type=MutationType.TAKE_RANDOM_NUMBER_OF_CAKES_RANDOM_CHILD
)

final_children, total_cookies = SolveWithEvolutionaryAlgorithm(data, parameters).evaluate_algorithm()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)