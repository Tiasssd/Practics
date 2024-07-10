# -*- coding: 1251 -*-
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import io

# Определение функции
def f(x):
    return (1/7 + np.log(np.sqrt(x))) * np.exp(x**2 - 2)

# Создание значений для X
x_values = np.linspace(1, 10, 100)
y_values = f(x_values)

# Создание графика с помощью matplotlib
plt.figure()
plt.plot(x_values, y_values, label="y = (1/7 + ln(sqrt(x))) * e^(x^2 - 2)")
plt.legend()
plt.title("График функции")

# Сохранение графика в PNG с помощью Pillow
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
img = Image.open(buf)
img.save('graph.png')
img.show()

# Закрытие буфера
buf.close()
