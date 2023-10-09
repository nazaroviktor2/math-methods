def jacoby(lower_diag, main_diag, upper_diag, b, x0, eps, max_iter, x_exact):
    n = len(b)
    x = x0.copy()
    xn = x.copy()
    max_exact = max(abs(x) for x in x_exact)
    max_vector = max(b)
    num = 0
    for iteration in range(max_iter):
        rel_error = 0
        rev_error = 0
        num += 1
        for i in range(n):
            left_x_prev = lower_diag[i] * (x[i - 1] if i > 0 else 0)
            right_x = upper_diag[i] * (x[i + 1] if i < n - 1 else 0)
            left_x = lower_diag[i] * (xn[i - 1] if i > 0 else 0)

            xn[i] = (b[i] - left_x_prev - right_x) / main_diag[i]

            rel_error = max(abs(xn[i] - x_exact[i]) / max_exact, rel_error)
            rev_error = max(abs(xn[i] * main_diag[i] + left_x + right_x - b[i]) / max_vector, rev_error)

        x = xn.copy()  # Обновляем x на новые значения

        if rel_error <= eps:
            break

    return x, num, rel_error, rev_error
