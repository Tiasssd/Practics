# -*- coding: 1251 -*-
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import io

# ����������� �������
def f(x):
    return (1/7 + np.log(np.sqrt(x))) * np.exp(x**2 - 2)

# �������� �������� ��� X
x_values = np.linspace(1, 10, 100)
y_values = f(x_values)

# �������� ������� � ������� matplotlib
plt.figure()
plt.plot(x_values, y_values, label="y = (1/7 + ln(sqrt(x))) * e^(x^2 - 2)")
plt.legend()
plt.title("������ �������")

# ���������� ������� � PNG � ������� Pillow
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
img = Image.open(buf)
img.save('graph.png')
img.show()

# �������� ������
buf.close()
