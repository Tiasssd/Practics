# -*- coding: 1251 -*-
import matplotlib.pyplot as plt
import numpy as np

def plot_microelements():
    microelements = ['������� C', '������� A', '���������', '�����������', '��������']
    values = [80, 60, 50, 40, 70]
    plt.figure(figsize=(15, 5))
    random_colors = np.random.rand(len(microelements), 3)

    plt.subplot(1, 2, 1)
    plt.bar(microelements, values, color=random_colors)
    plt.xlabel('�������������')
    plt.ylabel('��������')
    plt.title('���������� ���������')

    plt.subplot(1, 2, 2)
    plt.pie(values, labels=microelements, autopct='%1.1f%%', colors=random_colors)
    plt.title('�������� ���������')

    plt.tight_layout()
    plt.show()

plot_microelements()
