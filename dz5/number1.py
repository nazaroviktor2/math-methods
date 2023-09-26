import math


def newton(func, dif_func, x, e):
    count = 0
    f_x = func(x)
    df_x = dif_func(x)
    while f_x / df_x > e:
        count += 1
        x = x - f_x / df_x
        f_x = func(x)
        df_x = dif_func(x)
    return x


if __name__ == '__main__':
    a = lambda x: x ** 5 + x - 1
    a_dif = lambda x: 5 * x ** 4 + 1
    print("1) f(x) = x^5 + x - 1")
    print(f"x = {newton(a, a_dif, 1, 10 ** (-8)):.8f}")

    b = lambda x: 6 * x + 5 - math.sin(x)
    b_dif = lambda x: 6 + math.cos(x)
    print("2) f(x) = 6x + 5 - sin(x)")
    print(f"x = {newton(b, b_dif, 0, 10 ** (-8)):.8f}")

    c = lambda x: math.log(x) + x ** 2 - 3
    c_dif = lambda x: 1 / x + 2 * x
    print("3) f(x) = ln(x) + x^2 - 3")
    print(f"x = {newton(c, c_dif, 2, 10 ** (-8)):.8f}")
