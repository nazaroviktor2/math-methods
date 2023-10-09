from dz8.number1 import jacoby


def generate_data(n, main_elem, side_elem, b):
    lower_diag = [side_elem] * n
    main_diag = [main_elem] * n
    upper_diag = [side_elem] * n
    x0 = [0] * n

    return lower_diag, main_diag, upper_diag, b, x0


if __name__ == "__main__":
    for n in [100, 100000]:
        b = [2] + [1] * (n - 2) + [2]
        eps = 1e-6
        max_iter = 100000
        exact_solution = [1] * n
        solution = jacoby(*generate_data(n, 3, -1, b), eps, max_iter, exact_solution)
        print(f"n = {n}:")
        print(f"\titer: {solution[1]}")
        print(f"\terror: {solution[2]}")
        print(f"\trev_error: {solution[3]}")
        print("------------------------------")
