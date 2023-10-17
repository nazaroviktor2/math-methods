import matplotlib.pyplot as plt
import math

from dz11.number2 import midpoint


def compute_approximation_error(func, lower_limit, upper_limit, analytical_result, num_iterations):
    iteration_values = [2 ** i for i in range(num_iterations)]
    errors = []

    for num_intervals in iteration_values:
        result = midpoint(func, lower_limit, upper_limit, num_intervals)
        error = abs(result - analytical_result)
        errors.append(error)

    plt.loglog(iteration_values, errors, marker='o')
    plt.xlabel('Число интервалов (n)')
    plt.ylabel('Погрешность аппроксимации')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    num_iterations = 8
    task_a = lambda x: x / math.sqrt(x ** 2 + 9)
    compute_approximation_error(task_a, 0, 4, 2, num_iterations)
    task_b = lambda x: x ** 2 * math.log(x, math.e)

    compute_approximation_error(task_b, 1, math.pi, 6.9986217, num_iterations)
