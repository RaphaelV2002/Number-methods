import matplotlib.pyplot as plt
from numpy import arange
from numpy import meshgrid
import numpy as np
def Euler(a, b, h, x, u):
    print('x', 'u', 'y-u')
    n = int((b-a)/h)
    u = np.zeros(n+1)# Массив численных решений
    err = np.zeros(n+1)
    y = np.zeros(n+1)
    for i in range(n):
        u[i+1] = u[i] + h * fun(x+(h/2.0), u[i]+(h/2.0)*fun(x,u[i]))  # Численное решение
        y[i+1] = -1.0/(-x-1.0)  # Аналитическое решение
        err[i]=abs(y[i+1]-u[i+1])
        print(round(x, 3), round(u[i+1], 3), round(err[i], 3))
        x += h
    print(max(err))
    delta = 0.025
    xrange = arange(-100.0, 100.0, delta)
    yrange = arange(-100.0, 100.0, delta)
    x, y = meshgrid(xrange,yrange)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(x,u*100.0,"ro")
    plt.plot(x,y*100.0,"bo")
    plt.plot(x,err*100.0,"go")
    plt.grid()
    plt.show()
    return u


def fun(x, u):
    return (u*u-u)/x  # Функция


a = 1.0  # Начало сетки
b = 3.0  # Конец сетки
h = 0.01  # Шаг
x = 1.0  # Задача Коши
u = 0.5
Euler(a, b, h, x, u)
