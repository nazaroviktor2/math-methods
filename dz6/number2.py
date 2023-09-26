from dz6.number1 import gauss


def create_matrix(n):
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]


def gilibert(n):
    # Определение матрицы Гильберта n x n
    matrix_a = create_matrix(n)
    # Определение вектора b (все элементы равны 1)
    b_a = [1] * n
    # Решение системы линейных уравнений Hx = b
    result = gauss(matrix_a, b_a)
    print(f"n = {n}: result = {result}")


if __name__ == "__main__":
    gilibert(2)
    gilibert(5)
    gilibert(10)
