# -*- coding: 1251 -*-
file_name = input('������� �������� �����: ')
with open(file_name, 'r') as file:
    lines = file.readlines()
    �����_�������_������ = ''
    for line in lines:
        if len(�����_�������_������) < len(line):
            �����_�������_������ = line
    file_name = input('������� �������� �����, � ������� ����� ��������� ����� ������� �����������: ')
    with open(file_name, 'w') as file_1:
        file_1.write(�����_�������_������)