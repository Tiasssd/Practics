# -*- coding: 1251 -*-
import os
������� = {}
file_path = r'C:\Users\shekh\OneDrive\������� ����\��� ��������\���� 4\������� 9\�������'
for i in range (1,10):
	�������['������ ' + str(i)] = os.path.getsize(file_path + ' ' + str(i) + '.py')
for line in �������:
	print(line + ' - ' + str(�������[line]) + ' ���.')