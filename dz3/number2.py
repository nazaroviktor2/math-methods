import math

from bisect import bisect

if __name__ == '__main__':
    a = lambda x: 2 * x**3 - 6 * x - 1
    print("1) 2x^3−6𝑥−1=0")
    print(f"x = {bisect(a, [-2, -1], 10 ** -6)}")
    print(f"x = {bisect(a, [-0.5, 0.5], 10 ** -6)}")
    print(f"x = {bisect(a, [1, 2], 10 ** -6)}")

    b = lambda x: math.e ** (x - 2) + x ** 3 - x
    print("2) e^(x - 2) + x^3 - x = 0")
    print(f"x = {bisect(a, [-2, -1], 10 ** -6)}")
    print(f"x = {bisect(a, [-0.75, 0.25], 10 ** -6)}")
    print(f"x = {bisect(a, [1, 2], 10 ** -6)}")

    c = lambda x: 1 + 5 * x - 6 * x**3 - math.e ** (2 * x)
    print("3) 1 + 5x - 6x^3 - e^2x = 0")
    print(f"x = {bisect(a, [-2, -1], 10 ** -6)}")
    print(f"x = {bisect(a, [-0.25, 0.75], 10 ** -6)}")
    print(f"x = {bisect(a, [1, 2], 10 ** -6)}")


