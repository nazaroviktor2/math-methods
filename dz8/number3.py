def gauss_seudel(c, a, b, r, x0, answer, max_iter=10000, eps=1e-6):
    n = len(x0)
    iteration = 0
    relative_error = 1
    reverse_error = 0
    max_answer = max(answer)
    max_r = max(r)

    while iteration < max_iter and relative_error > eps:
        relative_error = 0

        for i in range(n):
            left = c * x0[i - 1] if i - 1 >= 0 else 0
            right = b * x0[i + 1] if i + 1 < n else 0
            result = (r[i] - left - right) / a
            relative_error = max(relative_error, abs(x0[i] - answer[i]) / max_answer)
            x0[i] = result

        iteration += 1

    for i in range(n):
        left = c * x0[i - 1] if i - 1 >= 0 else 0
        right = b * x0[i + 1] if i + 1 < n else 0
        reverse_error = max(reverse_error, abs((x0[i] * a + left + right - r[i]) / max_r))

    return iteration, relative_error, reverse_error
