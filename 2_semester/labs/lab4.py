from lab3 import solve_LU


def square_decomp(a: [[]]):
    n = len(a)
    t = []
    for i in range(n):
        t.append([])
        for j in range(n):
            t[i].append(0)

    for i in range(n):
        for j in range(n):
            if i == j == 0:
                t[i][j] = a[i][j] ** (1 / 2)
            elif i == 0 and j > 0:
                t[i][j] = a[i][j] / t[0][0]
            elif i == j and i > 0:
                sub = 0
                for k in range(i):
                    sub += t[k][i] ** 2
                t[i][j] = (a[i][j] - sub) ** (1 / 2)
            elif i < j:
                sub = 0
                for k in range(i):
                    sub += t[k][i] * t[k][j]
                t[i][j] = (a[i][j] - sub) / t[i][i]
            else:
                t[i][j] = 0
    return t


def transpose(m: [[]]):
    new_m = []
    n = len(m)
    for i in range(n):
        new_m.append([])
        for j in range(n):
            new_m[i].append(m[j][i])
    return new_m


def main():
    matrix = [
        [1, 2, 4],
        [2, 13, 23],
        [4, 23, 77]
    ]
    vec = [10, 50, 150]
    T = square_decomp(matrix)
    print(solve_LU(transpose(T), T, vec))


if __name__ == '__main__':
    main()
