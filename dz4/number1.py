import math


def fixed_iter(fun, initial, n):
    x = initial
    for i in range(n):
        x = fun(x)
    return x


if __name__ == '__main__':
    print("1) 𝑥^3 = 2𝑥 + 2")

    initial = 1.768
    tolerance = 100
    fun = lambda x: (2 * x + 2) ** (1 / 3)
    z = fixed_iter(fun, initial, tolerance)
    print(f"F(z) = {fun(z):.20f}")

    print("2) e^x + x = 7")

    fun = lambda x: math.log(7 - x)
    initial = 1.66
    z = fixed_iter(fun, initial, 10)
    print(f"F(z) = {fun(z):.20f}")

    print("3) e^x + sin(x) = 4")
    fun = lambda x: math.log(4 - math.sin(x))
    initial = 1.05
    z = fixed_iter(fun, initial, tolerance)
    print(f"F(z) = {fun(z):.20f}")
