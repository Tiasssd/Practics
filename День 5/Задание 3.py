# -*- coding:1251 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f1(x):
    return 5 * x + 2

def f2(x):
    return 2 * np.exp(np.sqrt(np.abs(x - 1))) - ((x - np.pi) / (x + np.pi))

def find_intersections(f, g, x0):
    intersections = []
    for x in x0:
        result = fsolve(lambda x: f(x) - g(x), x)
        if result not in intersections:
            intersections.append(result[0])
    return intersections

def plot_functions(intersections):
    x = np.linspace(-8, 10, 400)
    y1 = f1(x)
    y2 = f2(x)

    plt.plot(x, y1, '-r', label='y = 5x + 2')
    plt.plot(x, y2, '-b', label='y = 2e^(sqrt(|x-1|-1)) - ((x - pi) / (x + pi))')

    for point in intersections:
        plt.plot(point, f1(point), 'ko', markersize=5)
        plt.text(point, f1(point), f'({point:.2f}, {f1(point):.2f})')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Графики функций')
    plt.grid(True)
    plt.show()

# Начальные приближения для поиска точек пересечения
x0 = np.linspace(4, 6, 100)
intersections = find_intersections(f1, f2, x0)
plot_functions(intersections)
