import matplotlib.pyplot as plt

INTERPOLATION_FACTOR = 6


def calculate_deltas(points):
    return [points[i + 1] - points[i] for i in range(len(points) - 1)]


def calculate_second_derivatives(x_points, y_points, s_0, s_4):
    delta_x = calculate_deltas(x_points)
    delta_y = calculate_deltas(y_points)

    second_derivatives = [0] * len(x_points)
    second_derivatives[0] = INTERPOLATION_FACTOR / delta_x[0] * (delta_y[0] / delta_x[0] - s_0)

    for i in range(1, len(x_points) - 1):
        divided_y = delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1]
        second_derivatives[i] = INTERPOLATION_FACTOR / (delta_x[i - 1] + delta_x[i]) * divided_y

    second_derivatives[-1] = INTERPOLATION_FACTOR / delta_x[-1] * (s_4 - delta_y[-1] / delta_x[-1])

    return second_derivatives


def calculate_coefficients(x_points, y_points, second_derivatives):
    a = y_points[:-1]
    b = [0] * len(x_points)
    d = [0] * len(x_points)

    for i in range(len(x_points) - 1):
        coefficient = 2 * second_derivatives[i] + second_derivatives[i + 1]
        b[i] = calculate_deltas(y_points)[i] / calculate_deltas(x_points)[i] - calculate_deltas(x_points)[
            i] * coefficient / INTERPOLATION_FACTOR
        d[i] = (second_derivatives[i + 1] - second_derivatives[i]) / (
                    INTERPOLATION_FACTOR * calculate_deltas(x_points)[i])

    return a, b, d


def generate_spline(x_points, y_points, a, b, second_derivatives, d):
    x_spline = [x / 100 for x in range(400)]
    y_spline = [0] * len(x_spline)

    for i in range(len(x_points) - 1):
        for j in range(len(x_spline)):
            if x_points[i] <= x_spline[j] <= x_points[i + 1]:
                x_interval = x_spline[j] - x_points[i]
                y_spline[j] = (
                        a[i] + b[i] * x_interval + second_derivatives[i] / 2 * x_interval ** 2 + d[i] * x_interval ** 3
                )

    return x_spline, y_spline


def plot_spline(x_points, y_points, x_spline, y_spline):
    plt.plot(x_points, y_points, "o", label="Исходные точки")
    plt.plot(x_spline, y_spline, label="Кубический сплайн")
    plt.xlabel("x")
    plt.ylabel("S(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [1, 3, 3, 4, 2]
    s_0 = -2
    s_4 = 1

    second_derivatives = calculate_second_derivatives(x, y, s_0, s_4)
    a, b, d = calculate_coefficients(x, y, second_derivatives)
    x_spline, y_spline = generate_spline(x, y, a, b, second_derivatives, d)

    plot_spline(x, y, x_spline, y_spline)
