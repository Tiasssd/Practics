# -*- coding: 1251 -*-
import cv2
import numpy as np

def draw_sierpinski_triangle(img, depth, p1, p2, p3):
    if depth == 0:
        points = np.array([p1, p2, p3], np.int32)
        cv2.polylines(img, [points], isClosed=True, color=input_color)
    else:
        mid1 = (p1 + p2) // 2
        mid2 = (p2 + p3) // 2
        mid3 = (p1 + p3) // 2

        draw_sierpinski_triangle(img, depth - 1, p1, mid1, mid3)
        draw_sierpinski_triangle(img, depth - 1, mid1, p2, mid2)
        draw_sierpinski_triangle(img, depth - 1, mid3, mid2, p3)

# Создаем черное изображение
input_color = list(map(int,input('Введите нужный вам цвет: ').split()))
width, height = 800, 800
img = np.zeros((height, width, 3), dtype=np.uint8)

# Начальные точки треугольника
p1 = np.array([width // 2, 100])
p2 = np.array([100, height - 100])
p3 = np.array([width - 100, height - 100])

# Глубина рекурсии (увеличьте для более детализированного фрактала)
depth = 5

draw_sierpinski_triangle(img, depth, p1, p2, p3)

# Отобразим изображение
cv2.imshow("Sierpinski Triangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
