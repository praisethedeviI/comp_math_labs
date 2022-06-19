from numpy import linalg
import math


def richardson(mat, vec, k):
    a, b = __find_min_max_eig(mat)
    dim = len(vec)
    x = [[0 for _ in range(dim)]]

    it = 0
    while it < k:
        it += 1
        x.append([])
        t = 2 / ((a + b) + (b - a) * math.cos((2 * it - 1) * math.pi / (2 * k)))
        for i in range(dim):
            x[it].append(x[it - 1][i] -
                         __find_subtraction(x[it - 1], mat, vec, i) * t)

    return x[-1], it


def __find_min_max_eig(mat):
    eig = linalg.eig(mat)[0]
    return min(eig), max(eig)


def __find_subtraction(x, mat, vec, pos):
    sub = -vec[pos]
    for j in range(len(vec)):
        sub += mat[pos][j] * x[j]
    return sub


def main():
    mat = [
        [10, 3, 3, 1, 2, 1],
        [1, 14, 1, 3, 5, 1],
        [2, 1, 7, 1, 3, 2],
        [1, 2, 2, 12, 3, 1],
        [1, 4, 2, 2, 9, 1],
        [2, 1, 2, 5, 4, 8],
    ]
    vec = [4, 1, 4, 6, 3, 6]

    print(richardson(mat, vec, 16)[0])
    print(linalg.solve(mat, vec))


if __name__ == '__main__':
    main()
