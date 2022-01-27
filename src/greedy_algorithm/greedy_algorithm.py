import random

from typing import List

from src.utils.models import Child


def greedy_algorithm(children: List[Child], iterations: int):

    children_amount = len(children)

    for i in range(iterations):
        child_index = random.randrange(0, children_amount)

        child = children[child_index]
        prev_child = children[child_index - 1] if child_index - 1 >= 0 else None
        next_child = children[child_index + 1] if child_index + 1 < children_amount else None

        if prev_child is None:
            child.set_cookies(count_cookies_for_two_children(child, next_child))

        elif next_child is None:
            child.set_cookies(count_cookies_for_two_children(child, prev_child))
        else:
            child.set_cookies(count_cookies_for_three_children(child, prev_child, next_child))

    return children


def count_cookies_for_two_children(child, second_child):
    if child.mark > second_child.mark:
        return second_child.cookies + 1
    elif child.mark < second_child.mark:
        return 1
    else:
        return second_child.cookies


def count_cookies_for_three_children(child, prev_child, next_child):
    if child.mark < prev_child.mark and child.mark < next_child.mark:
        return 1
    elif child.mark > prev_child.mark and child.mark > next_child.mark:
        return max(prev_child.cookies, next_child.cookies) + 1
    else:
        if prev_child.mark == child.mark:
            return prev_child.cookies
        elif next_child.mark == child.mark:
            return next_child.cookies
        else:
            if prev_child.mark > next_child.mark:
                return next_child.cookies + 1
            else:
                return prev_child.cookies + 1
