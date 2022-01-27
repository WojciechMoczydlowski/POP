import random
import jsonlines
from dataclasses import asdict
from src.evolutionary_algorithm.models import EvolutionaryAlgorithmParameters, SelectionType, MutationType
from src.compare_algorithms.compare_algorithms import compare_algorithms

seed = 100

random.seed(100)


def save_cookies_numer_and_parameters(init_cookies, final_cookies: float, parameters: EvolutionaryAlgorithmParameters):
    with jsonlines.open('output1.jsonl', mode='a') as writer:
        writer.write({
            'init_cookies': init_cookies,
            'final_cookies': final_cookies,
            'parameters': asdict(parameters)
        })


def save_result_with_params(init_cookies, gr_result, ev_result, amount, min_mark, max_mark):
    with jsonlines.open('compare.jsonl', mode='a') as writer:
        writer.write({
            'init_cookies': init_cookies,
            'gr_result': gr_result,
            'ev_result': ev_result,
            'amount': amount,
            'min_mark': min_mark,
            'max_mark': max_mark,
        })


def main():
    min_mark = 1

    for i1, amount in enumerate([10, 100, 1000, 10000]):
        for i2, max_mark in enumerate([10, 100, 1000, 10000]):
            result = compare_algorithms(amount, min_mark, max_mark)
            save_result_with_params(result[0], result[1], result[2], amount, min_mark, max_mark)


main()
