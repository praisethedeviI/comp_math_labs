import numpy as np


def jacobi_method(A, f, it=10):
    n = len(f)
    x_prev = x = np.array([0.0] * n)

    for k in range(it):
        for i in range(n):
            S = sum([A[i, j] * x_prev[j] if i != j else 0 for j in range(n)])
            x[i] = (f[i] - S) / A[i, i]

        x_prev = x

    return x


def seidel_method(A, f, it=10):
    n = len(f)
    xp = x = np.array([0.0] * n)

    for k in range(it):
        for i in range(n):
            S1 = sum((A[i, j] * x[j] for j in range(i)))
            S2 = sum((A[i, j] * xp[j] for j in range(i + 1, n)))
            x[i] = (f[i] - S1 - S2) / A[i, i]

        xp = x

    return x


def main():
    mat = np.matrix([
        [9.2, 2.5, -3.7],
        [0.9, 9., 0.2],
        [4.5, -1.6, -10.3]
    ])
    vec = np.array([-17.5, 4.4, -22.1])
    print(jacobi_method(mat, vec))
    print(seidel_method(mat, vec))


if __name__ == '__main__':
    main()
