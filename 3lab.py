import math

a = 0.5
b = 1.0

x_dot = {
    1: 0.73,
    2: 0.52,
    3: 0.97,
    4: 0.73
}


def function(x):
    return x ** 2 + math.log(x + 5)


def eleven_derivative(x):
    return math.factorial(10) / (x + 5) ** 11


def difference(f_0, f_1):
    return f_0 - f_1


def main():
    count = 10
    h = (b - a) / count
    x = []
    f = [[]]
    for i in range(count + 1):
        x.append(a + h * i)
        f[0].append(function(x[i]))

    for i in range(count):
        f.append([])
        for j in range(count - i):
            f[i + 1].append(difference(f[i][j + 1], f[i][j]))

    print(*x)
    for i in range(count + 1):
        print(*f[i])
    print()

    # Первая Ньютона
    t = (x_dot[2] - x[0]) / h
    N_1 = 0.
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t - j)
        N_1 += t_product * f[i][0] / math.factorial(i)

    print(f'N_1 = f({x_dot[2]}) =', N_1)

    # Вторая Ньютона
    t = (x_dot[3] - x[-1]) / h
    N_2 = 0.
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t + j)
        N_2 += t_product * f[i][-1] / math.factorial(i)

    print(f'N_2 = f({x_dot[3]}) =', N_2)

    # x****
    pos = 0
    diff = h
    for i, elem in enumerate(x):
        if abs(elem - x_dot[4]) <= diff:
            diff = abs(elem - x_dot[4])
            pos = i

    t = (x_dot[4] - x[pos]) / h
    G_2 = float()
    # x[pos] > x****  =>  интерполяционная формула Гаусса назад
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            if j % 2 == 0:
                t_product *= (t + math.floor(j / 2))
            else:
                t_product *= (t - math.floor(j / 2))
        minus = 0 if i % 2 == 0 else 1
        position = pos - minus - math.floor(i / 2)
        G_2 += t_product * f[i][position] / math.factorial(i)

    print(f'G_2 = f({x_dot[4]}) =', G_2)

    print('\nСравним минимальное и максимальное значения d^11y/dx^11:')
    max_der = eleven_derivative(x[0])
    print(f'11 производная от x = {x[0]} равна {max_der}')
    min_der = eleven_derivative(x[len(x) - 1])
    print(f'11 производная от x = {x[len(x) - 1]} равна {min_der}')

    print('\nСравним минимальное и максимальное значения остаточных членов:')

    omega_dot = {
        2: 1.,
        3: 1.,
        4: 1.
    }

    for i in range(count + 1):
        for j in range(2, 5):
            omega_dot[j] *= (x_dot[j] - x[i])

    max_R = max_der * omega_dot[4] / math.factorial(count + 1)
    min_R = min_der * omega_dot[4] / math.factorial(count + 1)
    print(f'минимальная R равна {min_R}')
    print(f'максимальная R равна {max_R}')

    R_dot = {
        2: eleven_derivative(x_dot[2]) * omega_dot[2] / math.factorial(
            count + 1),
        3: eleven_derivative(x_dot[3]) * omega_dot[3] / math.factorial(
            count + 1),
        4: eleven_derivative(x_dot[4]) * omega_dot[4] / math.factorial(
            count + 1)
    }
    print('R** =', R_dot[2])
    print('R*** =', R_dot[3])
    print('R**** =', R_dot[4])
    print()
    print('f** =', function(x_dot[2]))
    print('f*** =', function(x_dot[3]))
    print('f**** =', function(x_dot[4]))
    print()
    print('N_1 - f** =', N_1 - function(x_dot[2]))
    print('N_2 - f*** =', N_2 - function(x_dot[3]))
    print('G_2 - f**** =', G_2 - function(x_dot[4]))


if __name__ == '__main__':
    main()
