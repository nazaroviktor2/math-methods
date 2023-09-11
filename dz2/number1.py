def horner(n, a, x):
    y = a[n]
    for i in range(n):
        y = y * x + a[n - i - 1]
    return y


a = [-1 if i % 2 == 0 else 1 for i in range(1, 101)]

n = len(a) - 1
x = 1.00001
h = horner(n, a, x)

gorner = (1 - x ** 100) / (1 + x)
print(f"Результат по функции = {h}")
print(f"Результат по горнеру = {gorner}")
print(f"Погрешность: {abs(h) - abs(gorner)}")
