# -*- coding: 1251 -*-
import math
x =  int(input('Введите значение x: '))
if x > 0:
    print(math.pow(math.tan(x), 2))
else:
    print(1 - 2 * math.tan(x))