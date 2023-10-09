from matplotlib import pyplot as plt

from dz7.number1 import tridiag_solve


def generate_diagonals(n):
    c = [-1] * n
    a = [2] * n
    b = [-1] * n
    r = [1] * n
    return n, c, a, b, r


if __name__ == '__main__':

    n_values = [5, 10, 50]

    for n in n_values:
        x = tridiag_solve(*generate_diagonals(n))
        print(f'n={n}:', x)
        plt.plot(range(n), x, label=f'n={n}')

    plt.xlabel('Индекс')
    plt.ylabel('Значение x')
    plt.legend()
    plt.show()
