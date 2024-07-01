# -*- coding: 1251 -*-
a = -100
b = -50
c = int(input('Введите первое положительное число: '))
d = int(input('Введите второе положительное число: '))
if(a > b and c > d):
    print(c - b)
    print(d + a)
elif(a < b and c > d):
    print(c - a)
    print(d + b)
elif(a > b and c < d):
    print(d - b)
    print(c + a)
else:
    print(d - a)
    print(c + b)