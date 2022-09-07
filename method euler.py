import numpy as np


def Euler(a, b, h, x, u):
    print('x', 'u', 'y-u')
    n = int((b-a)/h)
    um = np.zeros(n)  # Массив численных решений
    for i in range(n):
        u += h * fun(x, u)  # Численное решение
        y = -1.0/(-x-1.0)  # Аналитическое решение
        print(round(x, 3), round(u, 3), round(y-u, 3))
        x += h
        um[i] = u
    return um


def fun(x, u):
    return (u*u-u)/x  # Функция


a = 1.0  # Начало сетки
b = 3.0  # Конец сетки
h = 0.01  # Шаг
x = 1.0  # Задача Коши
u = 0.5
Euler(a, b, h, x, u)
