from src.utils.models import Children, Child


def calculate_cost(children: Children) -> float:
    if not check_if_configuration_of_children_with_cookies_is_valid(children):
        return 1000000000.0

    return sum([child.cookies for child in children])


def check_if_configuration_of_children_with_cookies_is_valid(children: Children) -> bool:
    """If children sit side by side, a child with higher mark must have more cookies than a child with lower mark."""
    previous_child = Child(0, 0)
    for child in children:
        if previous_child.mark > child.mark and child.cookies >= previous_child.cookies \
                or child.mark > previous_child.mark and previous_child.cookies >= child.cookies:
            return False
        previous_child = child
    return True

