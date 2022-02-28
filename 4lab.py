import math
from scipy.misc import derivative

# m - номер x (x_m)
# n - порядок формулы Лагранжа
# k - порядок дифференциала
m, n, k = 0, 3, 2

count = 10
a = 0.5
b = 1.0
h = (b - a) / count


def second_der(x):
    return 2 - (x + 5) ** (-2)


def fourth_der(x):
    return -6 * (x + 5) ** (-4)


def func(x):
    return x ** 2 + math.log(x + 5)


def interpolation(x, x0, x1, x2, x3):
    return func(x0) * ((x - x1) * (x - x2) * (x - x3)) / (
                   (x0 - x1) * (x0 - x2) * (x0 - x3)) + \
           func(x1) * ((x - x0) * (x - x2) * (x - x3)) / (
                   (x1 - x0) * (x1 - x2) * (x1 - x3)) + \
           func(x2) * ((x - x0) * (x - x1) * (x - x3)) / (
                   (x2 - x0) * (x2 - x1) * (x2 - x3)) + \
           func(x3) * ((x - x0) * (x - x1) * (x - x2)) / (
                   (x3 - x0) * (x3 - x1) * (x3 - x2))


def inter_der(x, x0, x1, x2, x3):
    return derivative(interpolation, x, dx=1e-6, args=(x0, x1, x2, x3), n=k)


def omega(x, x0, x1, x2, x3):
    return (x - x0) * (x - x1) * (x - x2) * (x - x3)


def remainder(x, xi, x0, x1, x2, x3):
    return fourth_der(xi) / math.factorial(n + 1) * \
           derivative(omega, x, dx=1e-6, n=k, args=(x0, x1, x2, x3))


def main():
    x = []
    y = []
    for i in range(count + 1):
        x.append(a + h * i)
        y.append(func(x[i]))

    print(f'L" = {inter_der(x[0], x[0], x[1], x[2], x[3])}')
    print(f'y" = {second_der(x[0])}')
    print(f'L" - y" = {inter_der(x[0], x[0], x[1], x[2], x[3]) - second_der(x[0])}')

    print(f'Остаточный член минимальный {remainder(x[0], x[0], x[0], x[1], x[2], x[3])}')
    print(f'Остаточный член максимальный {remainder(x[0], x[-1], x[0], x[1], x[2], x[3])}')


if __name__ == '__main__':
    main()
