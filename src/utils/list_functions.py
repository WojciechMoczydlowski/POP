from typing import List


def copy_list_of_list(list_to_copy: List[List[any]]):
    return [inner_list[:] for inner_list in list_to_copy]


def list_splitter(list_to_split, ratio):
    elements = len(list_to_split)
    middle = int(elements * ratio)
    return [list_to_split[:middle], list_to_split[middle:]]