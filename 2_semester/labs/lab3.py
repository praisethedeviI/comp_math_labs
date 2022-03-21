from lab2 import SLE


def LU_decomposition(matrix: [[]]):  # L'U' = A' - vw^t / a_11
    n = len(matrix)
    U = []
    L = []
    for i in range(n):
        U.append([])
        L.append([])
        for j in range(n):
            U[i].append(0)
            L[i].append(0)

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(n):
            if i <= j:
                sub = 0
                for k in range(i):
                    sub += L[i][k] * U[k][j]
                U[i][j] = matrix[i][j] - sub
            else:
                sub = 0
                for k in range(j):
                    sub += L[i][k] * U[k][j] / U[j][j]
                L[i][j] = matrix[i][j] - sub

    return L, U


def solve_LU(L: [[]], U: [[]], b: []):
    sle = SLE(L, b)
    sle.solve()
    y = sle.get_vec()
    sle = SLE(U, y)
    sle.reverse()
    x = sle.get_vec()
    return x


def main():
    matrix = [
        [1, 2, 3],
        [2, 5, 1],
        [4, 3, 1]
    ]
    b = [1, 1, 1]
    L, U = LU_decomposition(matrix)
    print(solve_LU(L, U, b))


if __name__ == '__main__':
    main()
