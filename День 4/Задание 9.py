# -*- coding: 1251 -*-
import os
словарь = {}
file_path = r'C:\Users\shekh\OneDrive\Рабочий стол\Дни практики\День 4\Задание 9\Задание'
for i in range (1,10):
	словарь['Задача ' + str(i)] = os.path.getsize(file_path + ' ' + str(i) + '.py')
for line in словарь:
	print(line + ' - ' + str(словарь[line]) + ' бит.')