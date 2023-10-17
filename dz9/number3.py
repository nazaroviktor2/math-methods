import numpy as np
import matplotlib.pyplot as plt


def plot_interpolation(x, y):
    x_graph = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    poly_coeff = np.polyfit(x, y, len(x) - 1)
    poly = np.poly1d(poly_coeff)
    y_interpolated = poly(x_graph)

    plt.scatter(x, y, color="red", label="Исходные точки")
    plt.plot(x_graph, y_interpolated, color="blue", label="Интерполирующий полином")
    y_values = np.sin(x_graph)
    plt.plot(x_graph, y_values, label="sin(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x = np.linspace(0, np.pi / 2, 4)
    y = np.sin(x)
    plot_interpolation(x, y)
