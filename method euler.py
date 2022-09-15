import numpy as np
import matplotlib.pyplot as plt


def Euler(a, b, h, x, u):
    print('x', 'u', 'y-u')
    n = int((b-a)/h)
    um = np.zeros(n)  # Массив численных решений
    ym = np.zeros(n)
    xm = np.zeros(n)
    err = np.zeros(n)
    for i in range(n):
        xm[i] = x
        um[i] = u
        u += h * fun(x, u+(h/2.0)*fun(x, u))  # Численное решение
        y = -1.0/(-x-1.0)  # Аналитическое решение
        ym[i] = y
        err[i] = abs(y-u)
        x += h
        print(round(x, 3), round(u, 3), round(err[i], 3))
    print(max(err))
    plt.plot(xm, um)
    plt.plot(xm, err*100)
    plt.show()
    return um


def fun(x, u):
    return (u*u-u)/x  # Функция


a = 1.0  # Начало сетки
b = 3.0  # Конец сетки
h = 0.01  # Шаг
x = 1.0  # Задача Коши
u = 0.5
Euler(a, b, h, x, u)
