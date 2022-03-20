def LU_decomposition(matrix: [[]]):
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


def main():
    matrix = [
        [1, 2, 3],
        [2, 5, 1],
        [4, 3, 1]
    ]
    print(LU_decomposition(matrix))


if __name__ == '__main__':
    main()
