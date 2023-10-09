import numpy as np
import matplotlib.pyplot as plt


def calculate_cubic_spline(x, y):
    segm_len = len(x) - 1

    h = np.zeros(segm_len)
    delta_i = np.zeros(segm_len)
    for i in range(segm_len):
        h[i] = x[i + 1] - x[i]
        delta_i[i] = y[i + 1] - y[i]

    coefficients_1 = np.zeros(segm_len)
    coefficients_2 = np.zeros(segm_len)
    c = np.zeros(segm_len + 1)
    b = np.zeros(segm_len + 1)
    d = np.zeros(segm_len + 1)

    for i in range(1, segm_len):
        coefficients_1[i] = 3 / h[i] * delta_i[i] - 3 / h[i - 1] * delta_i[i - 1]
        coefficients_2[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * coefficients_1[i - 1]
        c[i] = coefficients_1[i] / coefficients_2[i]

    for i in range(segm_len):
        b[i] = (y[i + 1] - y[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return c, b, d


def interpolate_cubic_spline(x, y, c, b, d):
    x_interp = np.linspace(min(x), max(x), 1000)
    y_interp = np.zeros_like(x_interp)

    for i in range(len(x) - 1):
        mask = (x_interp >= x[i]) & (x_interp <= x[i + 1])
        y_interp[mask] = y[i] + b[i] * (x_interp[mask] - x[i]) + c[i] * (x_interp[mask] - x[i]) ** 2 + d[i] * (
                    x_interp[mask] - x[i]) ** 3

    return x_interp, y_interp


def plot_cubic_spline(x, y, x_interp, y_interp):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, "o", label="Исходные точки")
    plt.plot(x_interp, y_interp, "-", label="Сплайн")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x = [0, 1, 2, 3]
    y = [3, 5, 4, 1]

    c, b, d = calculate_cubic_spline(x, y)
    print(f"bi = {list(b)}")
    print(f"ci = {list(c)}")
    print(f"di = {list(d)}")
    x_interp, y_interp = interpolate_cubic_spline(x, y, c, b, d)

    plot_cubic_spline(x, y, x_interp, y_interp)
