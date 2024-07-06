# -*- coding: 1251 -*-
f = open('mama.txt', 'w+')
f.write('asdfghjklq')
словарь = { 1 : 'a', 2 : 's', 3 : 'd', 4 : 'f', 5 : 'g', 6 : 'h', 7 : 'j', 8 : 'k', 9 : 'l', 10 : 'q'}
f.close()
f = open('mama.bin', 'w')
for i in range (1, 11):
    f.write(словарь[i] + '\n')
f.close()
