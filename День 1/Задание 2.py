# -*- coding: 1251 -*-
a = -100
b = -50
c = int(input('������� ������ ������������� �����: '))
d = int(input('������� ������ ������������� �����: '))
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