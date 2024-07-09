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
        print("����������, ������� �������� �������� ��� ������ � ������.")
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
        left(180 - angle)  # ������� �� ������ ����
        fd(h / sin(radians(angle)))  # ����� ����������
        left(270 + angle)  # �������������� �������, ����� ��������� � ������
        fd(cos(180 - angle)* (h / sin(radians(angle))))
    else:
        down()
        fd(w)
        left(180 - angle)  # ������� �� ������ ����
        fd(h / sin(radians(angle)))  # ����� ����������
        left(90 + angle)  # �������������� �������, ����� ��������� � ������
        fd(sin(angle)*h)

    end_fill()
    mainloop()

window = Tk()
window.title('������, ���!')
window.geometry('335x150')

lbl1 = Label(window, text='������� ������ �������������� � ��������:')
lbl1.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

lbl2 = Label(window, text='������� ������ �������������� � ��������:')
lbl2.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)

btn = Button(window, text='���������', command=clicked)
btn.grid(column=0, row=3)

window.mainloop()
