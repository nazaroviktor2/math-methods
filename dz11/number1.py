import math


def trapezoidal(func, lower_limit, upper_limit, num_intervals):
    interval_width = (upper_limit - lower_limit) / num_intervals
    x_values = [lower_limit + i * interval_width for i in range(num_intervals + 1)]

    integral = 0.5 * (func(lower_limit) + func(upper_limit))

    for i in range(1, num_intervals):
        integral += func(x_values[i])

    integral *= interval_width

    return integral


if __name__ == "__main__":
    task_a = lambda x: x / math.sqrt(x ** 2 + 9)

    print("a)")
    print("\tпри n=16:", trapezoidal(task_a, 0, 4, 16))
    print("\tпри n=32:", trapezoidal(task_a, 0, 4, 32))

    task_b = lambda x: x ** 2 * math.log(x, math.e)
    print("b)")
    print("\tпри n=16:", trapezoidal(task_b, 1, 3, 16))
    print("\tпри n=32:", trapezoidal(task_b, 1, 3, 32))
