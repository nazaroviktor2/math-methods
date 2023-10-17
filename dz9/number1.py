import numpy as np
import matplotlib.pyplot as plt


def evaluate_polynomial(x, x_axis, coefficients):
    res = coefficients[0]
    multiplier = 1
    for i in range(1, len(x_axis)):
        multiplier *= (x - x_axis[i - 1])
        res += coefficients[i] * multiplier
    return res


def plot_interpolating_polynomial(x, y, scope=None):
    n = len(x)
    poly_coeff = np.zeros(n)
    poly_coeff[0] = y[0]
    y_ax = y.copy()
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x[j] - x[j - i])
        poly_coeff[i] = y[i]
    x_interp = np.linspace(min(x), max(x), 1000) if scope is None else np.linspace(*scope)
    y_interp = [evaluate_polynomial(value, x, poly_coeff) for value in x_interp]

    plt.figure()

    plt.scatter(x, y_ax, label='Исходные данные', color='red')
    plt.plot(x_interp, y_interp, label='Интерполирующий полином', color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Интерполирующий полином')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    x = [1800, 1850, 1900, 2000]
    y = [280, 283, 291, 370]
    plot_interpolating_polynomial(x, y)
