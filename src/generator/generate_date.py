import random
from src.utils.child import Child
min_mark = 1
max_mark = 100


def generate_data(seed, amount):
    random.seed(seed)
    children = []

    for i in range(amount):
        random_number = random.randrange(min_mark, max_mark)
        child = Child(random_number, random_number)
        children.append(child)

    return children



