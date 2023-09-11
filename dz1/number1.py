from numpy import arange


def find_number(e: float = 1, step=2):
    if e + 1 == 1:
        return e
    return find_number(e / step)


arr = [find_number(step=i) for i in arange(2, 1, -0.01)]
print(f"Ответ: {max(arr)}")
print("Так как формат плавающей точки использует двоичную систему счисления наилучшей шаг=2")
