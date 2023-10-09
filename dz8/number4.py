from number3 import gauss_seudel


if __name__ == "__main__":
    solution = gauss_seudel(1, 2, 1, [1] + [0] * 98 + [-1], [0] * 100, answer=[1, -1] * 50, eps=10 ** (-3))
    print(f"iter: {solution[0]}")
    print(f"error: {solution[1]}")
    print(f"rev_error: {solution[2]}")
