# -*- coding: 1251 -*-
import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageDraw

def choose_color(entry):
    color = colorchooser.askcolor()[1]
    entry.delete(0, tk.END)
    entry.insert(0, color)

def create_custom_image():
    width, height = 400, 400
    background_color = entry_background.get()
    grid_color = entry_grid.get()
    outline_color = entry_outline.get()
    fill_color = entry_fill.get()

    img = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(img)

    for i in range(0, width, 40):
        draw.line((i, 0, i, height), fill=grid_color)
        draw.line((0, i, width, i), fill=grid_color)

    half_circle_bbox = (40, 40, 360, 360)
    draw.pieslice(half_circle_bbox, 270, 90, outline=outline_color, fill=fill_color)

    half_circle_bbox = (80, 80, 320, 320)
    draw.pieslice(half_circle_bbox, 270, 90, outline=outline_color, fill=background_color)

    img.save('custom_image_half_circle.png')
    img.show()

# Создание окна
root = tk.Tk()
root.title("Создание изображения")

# Ввод цветов
label_background = tk.Label(root, text="Цвет фона:")
label_background.pack()
entry_background = tk.Entry(root)
entry_background.insert(0, "white")
entry_background.pack()

button_choose_background = tk.Button(root, text="Выбрать цвет", command=lambda: choose_color(entry_background))
button_choose_background.pack()

label_grid = tk.Label(root, text="Цвет сетки:")
label_grid.pack()
entry_grid = tk.Entry(root)
entry_grid.insert(0, "gray")
entry_grid.pack()

button_choose_grid = tk.Button(root, text="Выбрать цвет", command=lambda: choose_color(entry_grid))
button_choose_grid.pack()

label_outline = tk.Label(root, text="Цвет линий фигуры:")
label_outline.pack()
entry_outline = tk.Entry(root)
entry_outline.insert(0, "black")
entry_outline.pack()

button_choose_outline = tk.Button(root, text="Выбрать цвет", command=lambda: choose_color(entry_outline))
button_choose_outline.pack()

label_fill = tk.Label(root, text="Цвет заливки фигуры:")
label_fill.pack()
entry_fill = tk.Entry(root)
entry_fill.insert(0, "red")
entry_fill.pack()

button_choose_fill = tk.Button(root, text="Выбрать цвет", command=lambda: choose_color(entry_fill))
button_choose_fill.pack()

# Кнопка "Окей"
button_ok = tk.Button(root, text="Окей", command=create_custom_image)
button_ok.pack()

root.mainloop()
