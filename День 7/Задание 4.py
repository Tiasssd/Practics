# -*- coding: 1251 -*-
from PIL import Image, ImageDraw

# Создаем новое изображение размером 1200x300 пикселей (можете изменить по своему усмотрению)
width, height = 1200, 300
image = Image.new("RGB", (width, height), color="darkgrey")
draw = ImageDraw.Draw(image)

# Размеры и расположение клавиш
key_width, key_height = 50, 50
keys = [
    # Первый ряд клавиш
    {"x": 100-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 170-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 240-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 310-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 380-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 450-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 520-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 590-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 660-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 730-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 800-50, "y": 50, "w": key_width, "h": key_height},
    {"x": 870-50, "y": 50, "w": key_width * 2, "h": key_height},
    {"x": 940-50, "y": 50, "w": key_width, "h": key_height},
   {"x": 1010-20, "y": 50, "w": key_width, "h": key_height},
   {"x": 1070-20, "y": 50, "w": key_width, "h": key_height},
   {"x": 1130-20, "y": 50, "w": key_width, "h": key_height},
    # Второй ряд клавиш
    {"x": 100 - 50, "y": 120, "w": key_width+20, "h": key_height},
    {"x": 170 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 240 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 310 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 380 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 450 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 520 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 590 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 660 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 730 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 800 - 35, "y": 120, "w": key_width, "h": key_height},
    {"x": 870 - 35, "y": 120, "w": key_width + 55, "h": key_height},
   {"x": 1010 - 20, "y": 120, "w": key_width, "h": key_height},
   {"x": 1070 - 20, "y": 120, "w": key_width, "h": key_height},
   {"x": 1130 - 20, "y": 120, "w": key_width, "h": key_height},
    # Третий ряд клавиш
    {"x": 100 - 50, "y": 190, "w": key_width+30, "h": key_height},
    {"x": 170 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 240 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 310 - 20, "y": 190, "w": key_width+250, "h": key_height},
    {"x": 380 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 450 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 520 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 590 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 660 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 730 - 20, "y": 190, "w": key_width, "h": key_height},
    {"x": 800 - 20, "y": 190, "w": key_width, "h": key_height},
   {"x": 1010 - 20, "y": 190, "w": key_width, "h": key_height},
   {"x": 1070 - 20, "y": 190, "w": key_width+50, "h": key_height},
   {"x": 1130 - 20, "y": 190, "w": key_width, "h": key_height},
    # Пример для клавиши Enter
    {"x": 850, "y": 190, "w": key_width + 40, "h": key_height},
    # ... (добавьте остальные клавиши)
]

# Рисуем клавиши
for key in keys:
    draw.rectangle([key["x"], key["y"], key["x"] + key["w"], key["y"] + key["h"]], fill="black")

# Сохраняем изображение в формате PNG
image.save("keyboard_rectangles.png")
image.show()
print("Изображение сохранено как 'keyboard_rectangles.png'")
