from dz9.number1 import plot_interpolating_polynomial

if __name__ == "__main__":
    x = [1994, 1995, 1996, 1997]
    y = [67.052, 68.008, 69.803, 72.024]
    last_value = plot_interpolating_polynomial(x, y)
    print("Феномен Рунге отсутствует")
