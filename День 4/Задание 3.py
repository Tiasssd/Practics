# -*- coding: 1251 -*-
file_name = input('������� �������� �����: ')
with open(file_name, 'r') as file:
    lines = file.readlines()
    counter = 1
    ������� = {}
    for line in lines:
        �������[counter] = line
        counter += 1
print(str(�������))