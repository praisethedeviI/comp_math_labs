import math
import matplotlib.pyplot as plt

a = 0.5
b = 1.0

x_dot = {
    1: 0.73,
    2: 0.52,
    3: 0.97,
    4: 0.73
}

x = []
y = []
i = 0
L_1 = 0.
L_2 = 0.


def function(x):
    return x ** 2 + math.log(x + 5)


def second_diff(x):
    return 2 - 1 / ((x + 5) ** 2)


def third_diff(x):
    return 2 / ((x + 5) ** 3)


def div_diff(x, y):
    return (function(y) - function(x)) / (y - x)


def first():
    print("\nПЕРВОЕ ЗАДАНИЕ\n")
    h = (b - a) / 10
    global x, y
    for i in range(11):
        x.append(a + h * i)
        y.append(function(x[i]))
    plt.figure()
    plt.ylabel('y')
    plt.xlabel('x')
    plt.plot(x, y)
    plt.show()
    print("x", *x)
    print("y", *y)


def second():
    print("\nВТОРОЕ ЗАДАНИЕ\n")
    d = math.fabs(x[0] - x_dot[1])
    global i
    i = 0
    for j in range(len(x)):
        new = math.fabs(x[j] - x_dot[1])
        if d > new and x[j] < x_dot[1]:
            d = new
            i = j
    global L_1
    print('Выберем x_i = ', x[i])
    print('x_i+1 = ', x[i + 1])
    print('x* =', x_dot[1])
    L_1 = function(x[i]) * (x_dot[1] - x[i + 1]) / (x[i] - x[i + 1]) + function \
        (x[i + 1]) * (x_dot[1] - x[i]) / (x[i + 1] - x[i])
    print("L_1 = ", L_1)


def third():
    print("\nТРЕТЬЕ ЗАДАНИЕ\n")
    omega = abs((x_dot[1] - x[i]) * (x_dot[1] - x[i + 1]))
    f_i = second_diff(x[i])
    f_i_1 = second_diff(x[i + 1])

    print("минимальное и максимальное значение f''(x) на отрезке [x_i, x_i+1]:",
          f_i, f_i_1)
    print("разница между ними", f_i_1 - f_i)

    R_i = f_i * omega / 2
    R_i_1 = f_i_1 * omega / 2

    print("минимальное и максимальное значение R_1(x):",
          R_i, R_i_1)
    print("разница между ними", R_i_1 - R_i)


def fourth():
    print("\nЧЕТВЕРТОЕ ЗАДАНИЕ\n")
    omega = abs((x_dot[1] - x[i]) * (x_dot[1] - x[i + 1]))
    R_i = second_diff(x[i]) * omega / 2
    R_i_1 = second_diff(x[i + 1]) * omega / 2
    R_dot = second_diff(x_dot[1]) * omega / 2
    print("R*", R_dot)
    print("R_max - R* =", R_i_1 - R_dot)
    print("R* - R_min =", R_dot - R_i)
    print("L_1(x*) - f(x*) =", L_1 - function(x_dot[1]))


def fifth():
    print("\nПЯТОЕ ЗАДАНИЕ\n")
    global L_2
    L_2 = function(x[i - 1]) * (x_dot[1] - x[i]) * (x_dot[1] - x[i + 1]) / (
            x[i - 1] - x[i]) / (x[i - 1] - x[i + 1]) + \
          function(
              x[i]) * (x_dot[1] - x[i - 1]) * (x_dot[1] - x[i + 1]) / (
                  x[i] - x[i - 1]) / (x[i] - x[i + 1]) + function(
        x[i + 1]) * (x_dot[1] - x[i]) * (x_dot[1] - x[i - 1]) / (
                  x[i + 1] - x[i - 1]) / (x[i + 1] - x[i])
    print("L_2 = ", L_2)


def sixth():
    print("\nШЕСТОЕ ЗАДАНИЕ\n")
    omega = abs(
        (x_dot[1] - x[i - 1]) * (x_dot[1] - x[i]) * (x_dot[1] - x[i + 1]))
    f_i = third_diff(x[i - 1])
    f_i_1 = third_diff(x[i + 1])
    print("Значения f'''_i-1 и f'''_i+1", f_i, f_i_1)

    R_i = f_i * omega / 2
    R_i_1 = f_i_1 * omega / 2
    print("минимальное и максимальное значение R_1(x):",
          '{0:.16f}'.format(R_i), '{0:.16f}'.format(R_i_1))


def seventh():
    print("\nСЕДЬМОЕ ЗАДАНИЕ\n")
    omega = abs(
        (x_dot[1] - x[i - 1]) * (x_dot[1] - x[i]) * (x_dot[1] - x[i + 1]))
    R_i = third_diff(x[i - 1]) * omega / 2
    R_i_1 = third_diff(x[i + 1]) * omega / 2
    R_dot = third_diff(x_dot[1]) * omega / 2

    print("R*", '{0:.16f}'.format(R_dot))
    print("R_max - R* =", R_i_1 - R_dot)
    print("R* - R_min =", R_dot - R_i)
    print("L_2(x*) - f(x*) =", '{0:.16f}'.format(L_2 - function(x_dot[1])))


def eighth():
    print("\nВОСЬМОЕ ЗАДАНИЕ\n")
    f_i_i_1 = div_diff(x[i], x[i + 1])
    print("f(i, i+1) = ", f_i_i_1)
    f_i_1_i = div_diff(x[i - 1], x[i])
    print("f(i-1, i) = ", f_i_1_i)
    f_3i = (f_i_i_1 - f_i_1_i) / (x[i + 1] - x[i - 1])
    print("f(i-1, i, i+1) = ", f_3i)
    print("L_1 = ", function(x[i]) + f_i_i_1 * (x_dot[1] - x[i]))
    print("L_2 = ",
          function(x[i - 1]) + f_i_1_i * (x_dot[1] - x[i - 1]) + f_3i * (
                      x_dot[1] - x[i - 1]) * (x_dot[1] - x[i]))


def main():
    first()
    second()
    third()
    fourth()
    fifth()
    sixth()
    seventh()
    eighth()


if __name__ == '__main__':
    main()
