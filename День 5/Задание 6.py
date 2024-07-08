# -*- coding: 1251 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
colormaps = ['viridis', 'plasma', 'inferno']
current_cmap = colormaps[0]

fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=colors, cmap=current_cmap)

def update_colormap(event):
    global current_cmap
    if event.key == '1':
        current_cmap = colormaps[0]
    elif event.key == '2':
        current_cmap = colormaps[1]
    elif event.key == '3':
        current_cmap = colormaps[2]
    scatter.set_cmap(current_cmap)
    plt.draw()

# ���������� ����������� ������� ��� ����������
plt.text(0.49, 1.11, '������� 1, ��� ������ �������� �������: Virdis', transform=ax.transAxes, ha='center')
plt.text(0.5, 1.06, '������� 2, ��� ������ �������� �������: Plasma', transform=ax.transAxes, ha='center')
plt.text(0.5, 1.01, '������� 3, ��� ������ �������� �������: Inferno', transform=ax.transAxes, ha='center')

fig.canvas.mpl_connect('key_press_event', update_colormap)
plt.show()
