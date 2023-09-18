from bisect import bisect

if __name__ == '__main__':
    print('1) f(x) = x^3 - 2')
    print(f"x = {bisect(lambda x:x**3 - 2, [1, 2], 10**(-8))}")
    print('2) f(x) = x^3 - 3')
    print(f"x = {bisect(lambda x: x ** 3 - 3, [1, 2], 10 ** (-8))}")
    print('3) f(x) = x^3 - 5')
    print(f"x = {bisect(lambda x: x ** 3 - 5, [1, 2], 10 ** (-8))}")
