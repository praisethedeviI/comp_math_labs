import math

# m - номер x (x_m)
# n - порядок формулы Лагранжа
# k - порядок дифференциала
m, n, k = 0, 3, 2

count = 10
a = 0.5
b = 1.0
h = (b - a) / count


def func(x):
    return x**2 + math.log(x + 5)


def diff(i, j):  # difference between x_i and x_j
    return (i - j) * h


def main():
    x = []
    y = []
    for i in range(count + 1):
        x.append(a + h * i)
        y.append(func(x[i]))
    print(*x)
    print(*y)


if __name__ == '__main__':
    main()