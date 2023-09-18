import math

from bisect import bisect


if __name__ == '__main__':
    v = lambda x: math.pi * x**2 * (1 - x / 3) - 1
    aim = 10**(-3)
    print(f"Ответ: при h = {bisect(v, [0, 2], aim)}; {bisect(v, [2,5], aim)}")
