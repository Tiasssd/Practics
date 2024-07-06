# -*- coding: 1251 -*-
file_one = open('mama.bin', 'rb+')
file_two = open('mama_copy.bin', 'wb+')
lines = file_one.readlines()
for line in lines:
    file_two.write(line);
file_one.close()
словарь = {
    0 : "Нулевая",
    1 : "Первая",
    2 : "Вторая",
    3 : "Третяя",
    4 : "Четвёртая",
    5 : "Пятая",
    6 : "Шестая",
    7 : "Седьмая",
    8 : "Восьмая",
    9 : "Девятая"
    }
counter = 0
file_two.seek(0,0)
for line in file_two.readlines():
    print(словарь[counter] + ' строка: ' + line.decode('1251'))
    counter += 1
file_two.close()