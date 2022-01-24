import random
from src.utils.models import Child


def generate_data(amount, min_mark, max_mark):
    children = []

    for i in range(amount):
        random_number = random.randrange(min_mark, max_mark)
        child = Child(random_number, random_number)
        children.append(child)

    return children



