# -*- coding:1251 -*-
from tkinter import *
from numpy import *
import matplotlib.pyplot as plt
from tkinter import messagebox

def generate_random_numbers():
    size = int(spinbox_size.get())
    distribution = distribution_var.get()

    if distribution == "Uniform":
        random_numbers = random.uniform(size=size)
    elif distribution == "Normal":
        random_numbers = random.normal(size=size)
    elif distribution == "Exponential":
        random_numbers = random.exponential(size=size)
    else:
        messagebox.showerror("Ошибка", "Выбрано недопустимое распределение.")
        return
    
    plt.bar(range(len(random_numbers)), random_numbers, color=plt.cm.Pastel1_r(random_numbers))
    plt.xlabel("Индекс")
    plt.ylabel("Случайные числа")
    plt.title("Гистограмма с использованием colormap")
    plt.show()

root = Tk()
root.title("Генератор случайных чисел")


label_size = Label(root, text="Введите размер массива:")
spinbox_size = Spinbox(root, from_=1, to=100)
label_distribution = Label(root, text="Выберите распределение:")
distribution_var = StringVar(value="Uniform")
radio_uniform = Radiobutton(root, text="Равномерное", variable=distribution_var, value="Uniform")
radio_normal = Radiobutton(root, text="Нормальное", variable=distribution_var, value="Normal")
radio_exponential = Radiobutton(root, text="Экспоненциальное", variable=distribution_var, value="Exponential")


color_map_var = StringVar(value='Pastel1_r')
label_color_map = Label(root, text="Выберите ColorMap:")
color_maps = ['Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r',]
color_map_menu = OptionMenu(root, color_map_var, *color_maps)


button_generate = Button(root, text="Генерировать и строить гистограмму", command=generate_random_numbers)

label_size.pack()
spinbox_size.pack()
label_distribution.pack()
radio_uniform.pack()
radio_normal.pack()
radio_exponential.pack()
label_color_map.pack()
color_map_menu.pack()
button_generate.pack()

root.mainloop()
