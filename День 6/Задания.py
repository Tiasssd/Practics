# -*- coding: 1251 -*-
from tkinter import *  
from numpy import*
from turtle import*
from tkinter import ttk 
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import*

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
        messagebox.showerror("������", "������� ������������ �������������.")
        return
    
    plt.bar(range(len(random_numbers)), random_numbers, color=plt.cm.Pastel1_r(random_numbers))
    plt.xlabel("������")
    plt.ylabel("��������� �����")
    plt.title("����������� � �������������� colormap")
    plt.show()

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
window.title("����� ���������� � ���������� PythonRu")  
window.geometry('500x500')  
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab3 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='������ ������')  
tab_control.add(tab2, text='������ ������')  
tab_control.add(tab3, text='������ ������')  

#
label = Label(tab1, text="������� ������ ����� ���������")
label.grid(column=0,row=0)

button1 = Button(tab1, text="Enter", command=clicked)
button1.grid(column=1,row=1)

txt = Entry(tab1, width=20)
txt.grid(column=0,row=1)
#

#
lbl1 = Label(tab2, text='������� ������ �������������� � ��������:')
lbl1.grid(column=0, row=0)

txt = Entry(tab2, width=10)
txt.grid(column=1, row=0)
txt.focus()

lbl2 = Label(tab2, text='������� ������ �������������� � ��������:')
lbl2.grid(column=0, row=1)

txt1 = Entry(tab2, width=10)
txt1.grid(column=1, row=1)

btn = Button(tab2, text='���������', command=clicked1)
btn.grid(column=0, row=3)
#

#
label_size = Label(tab3, text="������� ������ �������:")
spinbox_size = Spinbox(tab3, from_=1, to=100)
label_distribution = Label(tab3, text="�������� �������������:")
distribution_var = StringVar(value="Uniform")
radio_uniform = Radiobutton(tab3, text="�����������", variable=distribution_var, value="Uniform")
radio_normal = Radiobutton(tab3, text="����������", variable=distribution_var, value="Normal")
radio_exponential = Radiobutton(tab3, text="����������������", variable=distribution_var, value="Exponential")


color_map_var = StringVar(value='Pastel1_r')
label_color_map = Label(tab3, text="�������� ColorMap:")
color_maps = ['Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r',]
color_map_menu = OptionMenu(tab3, color_map_var, *color_maps)


button_generate = Button(tab3, text="������������ � ������� �����������", command=generate_random_numbers)

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

tab_control.pack(expand=1, fill='both')  
window.mainloop()
