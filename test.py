from typing import Union
from math import sqrt
from random import uniform, normalvariate


def mean(numbers: list[Union[int, float]]) -> Union[int, float]:
    return sum(numbers) / len(numbers)


def variance(n: list[Union[int, float]]) -> Union[int, float]:
    return mean([pow(number - mean(n), 2) for number in n])


def std(array: list[Union[int, float]]) -> Union[int, float]:
    return sqrt(variance(array))


def generates_matrix(start: float, end: float, numbers: int) -> list:
    matrix = []
    while len(matrix) < numbers:
        matrix.append(uniform(start, end))
    return matrix


def normal_distribution(m: Union[int, float], standard_deviation: float) -> float:
    return normalvariate(m, standard_deviation)

print(variance(generate_matrix(0.0, 5.0, 100000)))
