# -*- coding: 1251 -*-
file_one = open('mama.bin', 'rb+')
file_two = open('mama_copy.bin', 'wb+')
lines = file_one.readlines()
for line in lines:
    file_two.write(line);
file_one.close()
������� = {
    0 : "�������",
    1 : "������",
    2 : "������",
    3 : "������",
    4 : "��������",
    5 : "�����",
    6 : "������",
    7 : "�������",
    8 : "�������",
    9 : "�������"
    }
counter = 0
file_two.seek(0,0)
for line in file_two.readlines():
    print(�������[counter] + ' ������: ' + line.decode('1251'))
    counter += 1
file_two.close()