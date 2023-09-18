import math

from bisect import bisect

if __name__ == '__main__':
    print(f"1) x^3 = 9, x = {bisect(lambda x: x**3 - 9, [2, 3], eps=10**-6)}")
    print(f"2) 3x^3 + x^2 = x+5, x = {bisect(lambda x: 3 * x**3 + x**2 - x - 5, [1, 2], eps=10**-6)}")
    print(f"3) cos^2(x) + 6 = x , x = {bisect(lambda x: math.cos(x) ** 2 + 6 - x, [6, 7], eps=10**-6)}")
