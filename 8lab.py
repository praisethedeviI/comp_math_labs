import math


def func(x):
    return 0.5 * x ** 2 - math.cos(2 * x)


def dif(x):
    return x + 2 * math.sin(2*x)


def main():
    x = [5]
    for i in range(100):
        x.append(x[-1] - func(x[-1])/ dif(x[-1]))
    print(x[-1])

    x = [-5]
    for i in range(100):
        x.append(x[-1] - func(x[-1]) / dif(x[-1]))
    print(x[-1])


if __name__ == '__main__':
    main()
