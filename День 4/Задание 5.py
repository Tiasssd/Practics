# -*- coding: 1251 -*-
file_name = input('Введите название файла: ')
with open(file_name, 'r') as file:
    lines = file.readlines()
    самая_длинная_строка = ''
    for line in lines:
        if len(самая_длинная_строка) < len(line):
            самая_длинная_строка = line
    file_name = input('Введите название файла, в который нужно сохранить самое длинное предложение: ')
    with open(file_name, 'w') as file_1:
        file_1.write(самая_длинная_строка)