from math import sqrt, log
from typing import Callable, Union
import numpy as np


def simpson_method(f, intervals, a, b):
    x_points = np.linspace(a, b, intervals + 1)
    y = []
    for x in x_points:
        y.append(f(x))
    result = y[0] + y[intervals]

    h = (b - a) / intervals

    result += 4 * np.sum(y[1:intervals:2]) + 2 * np.sum(y[2:intervals - 1:2])

    result *= h / 3
    return result


if __name__ == '__main__':
    print('1) Точное значение: 2')
    f_a = lambda x: x / sqrt((x ** 2 + 9))
    s = simpson_method(f_a, 16, 0, 4)
    print(f'\tПри m = 16: S = {s}')
    s = simpson_method(f_a, 32, 0, 4)
    print(f'\tПри m = 32: S = {s}')

    print("2) Точное значение: 6.99862")
    f_b = lambda x: x ** 2 * log(x)
    s = simpson_method(f_b, 16, 1, 3)
    print(f'\tПри m = 16: S = {s}')
    s = simpson_method(f_b, 32, 1, 3)
    print(f'\tПри m = 32: S = {s}')
