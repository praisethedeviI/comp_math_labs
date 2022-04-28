eps = 10**(-5)


def simple_iter(mat, vec, e=eps):
    dim = len(vec)
    x = list()
    x.append([0 for i in range(dim)])
    it = 0
    flag = True
    while flag:
        max_dif = 0
        it += 1
        x.append([])
        for i in range(dim):
            val = vec[i]
            for j in range(dim):
                if i != j:
                    val -= mat[i][j] * x[it - 1][j]
            val /= mat[i][i]
            x[it].append(val)
        for i in range(dim):
            if abs(x[it][i] - x[it-1][i]) > max_dif:
                max_dif = abs(x[it][i] - x[it-1][i])
        if max_dif < e:
            flag = False
    return x[it], it


def main():
    mat = [
        [9.2, 2.5, -3.7],
        [0.9, 9., 0.2],
        [4.5, -1.6, -10.3]
    ]
    vec = [-17.5, 4.4, -22.1]
    print(simple_iter(mat, vec))


if __name__ == '__main__':
    main()