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
        [10.9, 1.2, 2.1, 0.9],
        [1.2, 11.2, 1.5, 2.5],
        [2.1, 1.5, 9.8, 1.3],
        [0.9, 2.5, 1.3, 12.1]
    ]
    vec = [-7.0, 5.3, 10.3, 24.6]
    T = square_decomp(matrix)
    print(T)
    print(solve_LU(transpose(T), T, vec))


if __name__ == '__main__':
    main()
