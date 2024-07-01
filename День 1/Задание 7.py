# -*- coding: 1251 -*-
a = int(input('Введите шестизначное число: '))
count = 1
b = a
b //= 10
while b > 0:
    count += 1
    b //= 10
if (count != 6):
    print('Неверное количество разрядов у числа.')
    exit(0)
else: 
    _sum = 0
    while(a):
        _sum += a % 10
        a //= 10
print(str(_sum))