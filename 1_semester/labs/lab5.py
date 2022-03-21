import math

n = 4
t = [
    0.861136,
    0.339981,
    -0.339981,
    -0.861136
]
c = [
    0.347855,
    0.652145,
    0.652145,
    0.347855
]
a = 0.5
b = 1.0


def func(x):
    return x ** 2 + math.log(x + 5)


def find_x(a, b, t):
    return (b + a) / 2 + (b - a) * t / 2


def find_I(a, b):
    return ((b - a) / 2) * (c[0] * func(find_x(a, b, t[0])) +
                            c[1] * func(find_x(a, b, t[1])) +
                            c[2] * func(find_x(a, b, t[2])) +
                            c[3] * func(find_x(a, b, t[3])))


def main():
    I_n = find_I(a, b)
    m = (a + b) / 2
    I_2n = find_I(a, m) + find_I(m, b)
    eps = 0.000001
    I_4n = find_I(a, (a + m) / 2) + find_I((a + m) / 2, m) + find_I(m, (
                m + b) / 2) + find_I((m + b) / 2, b)
    print('I_n =',I_n)
    print('I_2n =',I_2n)
    print('I_4n =',I_4n)
    print('I_4n - I_2n =',I_4n - I_2n)


if __name__ == '__main__':
    main()
