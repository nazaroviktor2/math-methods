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


if __name__ == "__main__":
    radius = lambda x: 2 / 3 * math.pi * x ** 3 + 1 / 3 * math.pi * x ** 2 * 10 - 60
    radius_dif = lambda x: 2 * math.pi * x ** 2 + 20 / 3 * math.pi * x

    print('S = PI * R^2')
    print("f(R) = 2/3 * PI * R^3 + 1/3 * PI * R^2 * h - V")
    r = newton(radius, radius_dif, 3, 10 ** (-6))
    print(f"R = {r:.6f}")
