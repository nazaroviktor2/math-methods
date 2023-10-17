from dz9.number1 import plot_interpolating_polynomial

if __name__ == "__main__":
    print("В 1980 году: ")
    x = [1970, 1990]
    y = [3707475887, 5281653820]
    plot_interpolating_polynomial(x, y)
    print(f"\ta) 5281653820")

    x = [1960, 1970, 1990]
    y = [3039585530, 3707475887, 5281653820]
    plot_interpolating_polynomial(x, y)
    print(f"\tb) 5281653820")

    x = [1960, 1970, 1990, 2000]
    y = [3039585530, 3707475887, 5281653820, 6079603571]
    plot_interpolating_polynomial(x, y)
    print(f"\tc) 6079603571")
