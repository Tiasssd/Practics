# -*- coding: 1251 -*-

def �������(��������_�����):
    ������ = '\|/\|/\|/\|/\|/\|/\|/\|/\|/\|/'
    with open(��������_�����, "w") as file:
        for i in range(0,10):
            if i % 2 == 0:
                file.write(������ + "\n")
            else:
                file.write(������[::-1] + "\n")

��������_����� = input('������� �������� �����, ���� ����� ��������� �������: ')
�������(��������_�����)