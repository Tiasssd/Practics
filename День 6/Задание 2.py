# -*- coding:1251 -*-
from tkinter import *
from turtle import *
from math import *

def clicked1():
    try:
        h = int(txt.get())
        w = int(txt1.get())
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

window = Tk()
window.title('Привет, мир!')
window.geometry('335x150')

lbl1 = Label(window, text='Введите высоту прямоугольника в пикселях:')
lbl1.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

lbl2 = Label(window, text='Введите ширину прямоугольника в пикселях:')
lbl2.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)

btn = Button(window, text='Построить', command=clicked)
btn.grid(column=0, row=3)

window.mainloop()
