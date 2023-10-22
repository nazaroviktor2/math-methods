import math

from dz12.number1 import simpson_method

if __name__ == '__main__':
    print('1) y = x^3, x ∈ [0, 1]')
    s = simpson_method(lambda x: math.sqrt(1 + 3 * (x ** 4)), 32, 0, 1)
    print(f'\tДлина кривой = {s}')

    print('2) y = sin(x), x ∈ [0, pi]')
    s = simpson_method(lambda x: math.sqrt(1 + math.cos(x) ** 2), 32, 0, math.pi)
    print(f'\tДлина кривой = {s}')
