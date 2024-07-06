# -*- coding: 1251 -*-
file_name = input('Введите название файла: ')
with open(file_name, 'r') as file:
    lines = file.readlines()
    counter = 1
    словарь = {}
    for line in lines:
        словарь[counter] = line
        counter += 1
print(str(словарь))