# -*- coding: 1251 -*-
def проверка(x,y):
    if x > 4 or x < -4 or y > 4 or y < -3:
        return 'не принадлежат выделенной области'
    elif x > 1 or x < -2 and y > 0:
        return 'не принадлежат выделенной области'
    else:
        return 'принадлежат выделенной области'

x, y = input('Введите x, y: ').split()
x, y = float(x), float(y)
print('Координаты ' + проверка(x,y))