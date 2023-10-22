from math import exp
import matplotlib.pyplot as plt


def central_difference(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


def approximate_function(func):
    derivative = func(0)
    h_values = [10 ** -i for i in range(1, 17)]
    errors = []

    for h in h_values:
        approx_derivative = central_difference(func, 0, h)
        errors.append(abs(approx_derivative - derivative))
    plt.loglog(h_values, errors, marker='o')
    plt.xlabel('Значение h')
    plt.ylabel('Ошибка аппроксимации')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    approximate_function(lambda x: exp(x))
