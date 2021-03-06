import math
import pytest

from src.utils.cost_function import calculate_cost, check_if_configuration_of_children_with_cookies_is_valid
from src.utils.models import Child


@pytest.mark.parametrize(
    "children,result",
    [
        ([Child(5, 1), Child(4, 2), Child(3, 1)], False),
        ([Child(5, 1), Child(4, 2), Child(3, 1)], False),
        ([Child(3, 1), Child(4, 2), Child(3, 0)], True),
        ([Child(4, 2), Child(4, 2), Child(3, 0)], True),
        ([Child(4, 2), Child(3, 2), Child(2, 2)], False),
        ([Child(19, 1), Child(59, 1), Child(59, 1)], False),
    ])
def test_check_if_configuration_of_children_with_cookies_is_valid(children, result):
    assert check_if_configuration_of_children_with_cookies_is_valid(children) == result


@pytest.mark.parametrize(
    "children,result",
    [([Child(5, 1), Child(4, 2), Child(3, 1)], math.inf),
     ([Child(5, 1), Child(4, 2), Child(3, 1)], math.inf),
     ([Child(3, 1), Child(4, 2), Child(3, 0)], 3)]
)
def test_cost_function_result(children, result):
    assert calculate_cost(children) == result
