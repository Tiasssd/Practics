# -*- coding: 1251 -*-
from tkinter import *  
from numpy import random  # Исправлено: импорт конкретного модуля random из numpy
from turtle import *  
from tkinter import ttk 
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import *

def generate_random_numbers():
    size = int(spinbox_size.get())
    distribution = distribution_var.get()

    if distribution == "Uniform":
        random_numbers = random.uniform(size=size)  # Исправлено: random.uniform(low=0.0, high=1.0, size=None)
    elif distribution == "Normal":
        random_numbers = random.normal(size=size)  # Исправлено: random.normal(loc=0.0, scale=1.0, size=None)
    elif distribution == "Exponential":
        random_numbers = random.exponential(size=size)  # Исправлено: random.exponential(scale=1.0, size=None)
    else:
        messagebox.showerror("Ошибка", "Выбрано недопустимое распределение.")
        return
    
    plt.bar(range(len(random_numbers)), random_numbers, color=plt.cm.get_cmap(color_map_var.get())(random_numbers))  # Исправлено: использование get_cmap
    plt.xlabel("Индекс")
    plt.ylabel("Случайные числа")
    plt.title("Гистограмма с использованием colormap")
    plt.show()

def clicked():
    reset()
    shape('turtle')
    color('black')
    width_value = txt.get()
    print(f"Значение из txt: '{width_value}'")  # Отладочное сообщение
    try:
        width(int(width_value))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите числовое значение для ширины следа черепашки.")
        return
    down()
    left(90)
    fd(50)
    right(90)
    fd(30)
    right(90)
    fd(30)
    left(90)
    fd(30)
    left(90)
    fd(30)
    right(90)
    fd(30)
    right(90)
    fd(50)
    left(90)
    fd(30)
    exitonclick()
    mainloop()

def clicked1():
    try:
        h = int(txt1.get())
        w = int(txt2.get())
        angle = degrees(atan(h/w))
    except ValueError:
        print("Пожалуйста, введите числовые значения для высоты и ширины.")
        return
    screensize(1200,1200,'orange')
    reset()
    shape('turtle')
    color('red', 'green')
    width(5)
    begin_fill()

    if h > w:
        down()
        fd(w)
        left(180 - angle)  # Поворот на нужный угол
        fd(h / sin(radians(angle)))  # Длина гипотенузы
        left(270 + angle)  # Дополнительный поворот, чтобы вернуться к началу
        fd(cos(180 - angle)* (h / sin(radians(angle))))
    else:
        down()
        fd(w)
        left(180 - angle)  # Поворот на нужный угол
        fd(h / sin(radians(angle)))  # Длина гипотенузы
        left(90 + angle)  # Дополнительный поворот, чтобы вернуться к началу
        fd(sin(angle)*h)

    end_fill()
    mainloop()

def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Ошибка", "Ошибка вычисления")

def move(direction):
    global current_position, steps
    row, col = current_position
    if direction == "up":
        new_position = (row - 1, col)
    elif direction == "down":
        new_position = (row + 1, col)
    elif direction == "left":
        new_position = (row, col - 1)
    elif direction == "right":
        new_position = (row, col + 1)
    else:
        return

    if (0 <= new_position[0] < ROWS and 0 <= new_position[1] < COLS and
            maze[new_position[0]][new_position[1]] == 0):
        current_position = new_position
        steps += 1
        canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill="white")
        canvas.create_rectangle(new_position[1] * 50, new_position[0] * 50, (new_position[1] + 1) * 50, (new_position[0] + 1) * 50, fill="blue")
        if current_position == end:
            messagebox.showinfo("Поздравляем!", f"Вы достигли точки B за {steps} шагов!")
    else:
        messagebox.showwarning("Ошибка", "Движение в выбранном направлении невозможно.")

def on_key_press(event):
    if event.char == 'w':
        move("up")
    elif event.char == 's':
        move("down")
    elif event.char == 'a':
        move("left")
    elif event.char == 'd':
        move("right")

window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('600x600')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab3 = ttk.Frame(tab_control)  
tab4 = ttk.Frame(tab_control)  
tab5 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Первая задача')  
tab_control.add(tab2, text='Вторая задача')  
tab_control.add(tab3, text='Третья задача')  
tab_control.add(tab4, text='Четвёртая задача')  
tab_control.add(tab5, text='Пятая задача')  

#
label = Label(tab1, text="Введите ширину следа черепашки")
label.grid(column=0,row=0)

button1 = Button(tab1, text="Enter", command=clicked)
button1.grid(column=1,row=1)

txt = Entry(tab1, width=20)
txt.grid(column=0,row=1)
#

#
lbl1 = Label(tab2, text='Введите высоту прямоугольника в пикселях:')
lbl1.grid(column=0, row=0)

txt1 = Entry(tab2, width=10)
txt1.grid(column=1, row=0)
txt1.focus()

lbl2 = Label(tab2, text='Введите ширину прямоугольника в пикселях:')
lbl2.grid(column=0, row=1)

txt2 = Entry(tab2, width=10)
txt2.grid(column=1, row=1)

btn = Button(tab2, text='Построить', command=clicked1)
btn.grid(column=0, row=3)
#

#
label_size = Label(tab3, text="Введите размер массива:")
spinbox_size = Spinbox(tab3, from_=1, to=100)
label_distribution = Label(tab3, text="Выберите распределение:")
distribution_var = StringVar(value="Uniform")
radio_uniform = Radiobutton(tab3, text="Равномерное", variable=distribution_var, value="Uniform")
radio_normal = Radiobutton(tab3, text="Нормальное", variable=distribution_var, value="Normal")
radio_exponential = Radiobutton(tab3, text="Экспоненциальное", variable=distribution_var, value="Exponential")

color_map_var = StringVar(value='Pastel1_r')
label_color_map = Label(tab3, text="Выберите ColorMap:")
color_maps = ['Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r']
color_map_menu = OptionMenu(tab3, color_map_var, *color_maps)

button_generate = Button(tab3, text="Генерировать и строить гистограмму", command=generate_random_numbers)

label_size.pack()
spinbox_size.pack()
label_distribution.pack()
radio_uniform.pack()
radio_normal.pack()
radio_exponential.pack()
label_color_map.pack()
color_map_menu.pack()
button_generate.pack()
#

#
entry = Entry(tab4, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

button_1 = Button(tab4, text="1", padx=20, pady=20, command=lambda: button_click("1"))
button_2 = Button(tab4, text="2", padx=20, pady=20, command=lambda: button_click("2"))
button_3 = Button(tab4, text="3", padx=20, pady=20, command=lambda: button_click("3"))
button_4 = Button(tab4, text="4", padx=20, pady=20, command=lambda: button_click("4"))
button_5 = Button(tab4, text="5", padx=20, pady=20, command=lambda: button_click("5"))
button_6 = Button(tab4, text="6", padx=20, pady=20, command=lambda: button_click("6"))
button_7 = Button(tab4, text="7", padx=20, pady=20, command=lambda: button_click("7"))
button_8 = Button(tab4, text="8", padx=20, pady=20, command=lambda: button_click("8"))
button_9 = Button(tab4, text="9", padx=20, pady=20, command=lambda: button_click("9"))
button_0 = Button(tab4, text="0", padx=20, pady=20, command=lambda: button_click("0"))
button_dot = Button(tab4, text=".", padx=22, pady=20, command=lambda: button_click("."))

button_add = Button(tab4, text="+", padx=20, pady=20, command=lambda: button_click("+"))
button_subtract = Button(tab4, text="-", padx=22, pady=20, command=lambda: button_click("-"))
button_multiply = Button(tab4, text="*", padx=22, pady=20, command=lambda: button_click("*"))
button_divide = Button(tab4, text="/", padx=22, pady=20, command=lambda: button_click("/"))
button_square = Button(tab4, text="^2", padx=16, pady=20, command=lambda: button_click("**2"))
button_open_bracket = Button(tab4, text="(", padx=22, pady=20, command=lambda: button_click("("))
button_close_bracket = Button(tab4, text=")", padx=22, pady=20, command=lambda: button_click(")"))
button_equal = Button(tab4, text="=", padx=20, pady=20, command=calculate)
button_clear = Button(tab4, text="C", padx=20, pady=20, command=clear)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_square.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

button_open_bracket.grid(row=5, column=0)
button_close_bracket.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column=3)
#

#
ROWS = 10
COLS = 10

maze = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
]

start = (9, 9)
end = (0, 0)

current_position = start
steps = 0

canvas = Canvas(tab5, width=COLS * 50, height=ROWS * 50)
canvas.pack()

for row in range(ROWS):
    for col in range(COLS):
        if maze[row][col] == 1:
            if row > 0 and maze[row-1][col] == 0:
                canvas.create_line(col * 50, row * 50, (col + 1) * 50, row * 50, fill="black", width=2)
            if row < ROWS - 1 and maze[row+1][col] == 0:
                canvas.create_line(col * 50, (row + 1) * 50, (col + 1) * 50, (row + 1) * 50, fill="black", width=2)
            if col > 0 and maze[row][col-1] == 0:
                canvas.create_line(col * 50, row * 50, col * 50, (row + 1) * 50, fill="black", width=2)
            if col < COLS - 1 and maze[row][col+1] == 0:
                canvas.create_line((col + 1) * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill="black", width=2)

canvas.create_rectangle(start[1] * 50, start[0] * 50, (start[1] + 1) * 50, (start[0] + 1) * 50, fill="blue")
canvas.create_rectangle(end[1] * 50, end[0] * 50, (end[1] + 1) * 50, (end[0] + 1) * 50, fill="red")

frame = Frame(tab5)
frame.pack()

Button(frame, text="Вверх", command=lambda: move("up")).grid(row=0, column=1)
Button(frame, text="Влево", command=lambda: move("left")).grid(row=1, column=0)
Button(frame, text="Вправо", command=lambda: move("right")).grid(row=1, column=2)
Button(frame, text="Вниз", command=lambda: move("down")).grid(row=2, column=1)

window.bind("<Key>", on_key_press)
#

tab_control.pack(expand=1, fill='both')  
window.mainloop()
