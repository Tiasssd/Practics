# -*- coding: 1251 -*-
def ��������(x,y):
    if x > 4 or x < -4 or y > 4 or y < -3:
        return '�� ����������� ���������� �������'
    elif x > 1 or x < -2 and y > 0:
        return '�� ����������� ���������� �������'
    else:
        return '����������� ���������� �������'

x, y = input('������� x, y: ').split()
x, y = float(x), float(y)
print('���������� ' + ��������(x,y))