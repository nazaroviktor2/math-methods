def fixed_iter(fun, x0, n):
    x = x0
    for i in range(n):
        x = fun(x)
    return x

if __name__ == '__main__':

    tolerance = 100
    initial = 1.0

    fun1 = lambda x: (2 * x + 2/x**2) / 3
    fun2 = lambda x: (2 * x + 3/x**2) / 3
    fun3 = lambda x: (2 * x + 5/x**2) / 3

    val = fixed_iter(fun1, initial, tolerance)
    print(f"Кубический корень для A = 2: {val:.53f}")
    val = fixed_iter(fun2, initial, tolerance)
    print(f"Кубический корень для A = 3: {val:.53f}")
    val = fixed_iter(fun3, initial, tolerance)
    print(f"Кубический корень для A = 5: {val:.53f}")
