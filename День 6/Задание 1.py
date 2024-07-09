# -*- coding: 1251 -*-
from turtle import*
from tkinter import*

def clicked():
    reset()
    shape('turtle')
    color('black')
    width(txt.get())
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

window = Tk()
window.title('Задача 1')

label = Label(window, text="Введите ширину следа черепашки")
label.grid(column=0,row=0)

button1 = Button(window, text="Enter", command=clicked)
button1.grid(column=1,row=1)

txt = Entry(window, width=20)
txt.grid(column=0,row=1)

window.geometry('250x250')
window.mainloop()

