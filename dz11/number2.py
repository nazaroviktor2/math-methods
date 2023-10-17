import math


def midpoint(f, start, end, num_intervals):
    step = (end - start) / num_intervals
    approximation = 0

    for i in range(num_intervals):
        midpoint = start + (i + 0.5) * step
        approximation += f(midpoint)

    # Умножаем на шаг для получения приближенного интеграла
    approximation *= step

    return approximation


if __name__ == "__main__":
    task_a = lambda x: x / math.sin(x)
    print("a)")
    print("\tпри n=16:", midpoint(task_a, 0, math.pi, 16))
    print("\tпри n=32:", midpoint(task_a, 0, math.pi, 32))

    task_b = lambda x: math.atan(x) / x
    print("b)")
    print("\tпри n=16:", midpoint(task_b, 0, 1, 16))
    print("\tпри n=32:", midpoint(task_b, 0, 1, 32))
