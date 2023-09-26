def gauss_elimination(matrix, equ):
    # Расширяем матрицу для хранения правых частей уравнений
    for i, row in enumerate(matrix):
        row.append(equ[i])

    matrix_len = len(matrix)

    for i in range(matrix_len):
        # Находим максимальный элемент в столбце i для выбора главного элемента
        max_row = max(range(i, matrix_len), key=lambda x: abs(matrix[x][i]))

        # Меняем строки местами
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Приводим текущий столбец к единичному элементу
        pivot = matrix[i][i]
        for j in range(i, matrix_len + 1):
            matrix[i][j] /= pivot

        # Обнуляем элементы ниже текущего
        for k in range(i + 1, matrix_len):
            factor = matrix[k][i]
            for j in range(i, matrix_len + 1):
                matrix[k][j] -= factor * matrix[i][j]

    return matrix


def back_substitution(matrix):
    matrix_len = len(matrix)
    x = [0] * matrix_len

    for i in range(matrix_len - 1, -1, -1):
        x[i] = matrix[i][-1]
        for j in range(i + 1, matrix_len):
            x[i] -= matrix[i][j] * x[j]

    return x


def gauss(matrix, equ):
    matrix = gauss_elimination(matrix, equ)
    return back_substitution(matrix)


if __name__ == '__main__':
    matrix = [
        [2, -2, -1],
        [4, 1, -2],
        [-2, 1, -1]
    ]
    equ = [-2, 1, -3]
    result = gauss(matrix, equ)

    print(f"Решение: {result}")
