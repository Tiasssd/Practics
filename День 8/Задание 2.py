# -*- coding: 1251 -*-
import tkinter as tk
from tkinter import messagebox
import random
import pygame

# ������� � ������
questions = [
    ("����� ���� � ����?", "�����", "�������", "�������", "������", 1),
    ("������� ��� � �����?", "6", "8", "10", "12", 2),
    ("����� ����� ������� �����?", "�������������", "���������", "�������� ���������", "�����", 4),
    ("������� ������ � ��������� �������?", "7", "8", "9", "10", 2),
    ("����� ��� ��������� ��� �������?", "����", "��������", "�������", "���������� ���", 2),
    ("����� ����� ������� ������� � ����?", "������", "�������", "��������", "������", 1),
    ("����� ����� ������� ���������?", "������", "����", "������", "����������", 2),
    ("����� ����� ��������� ���������?", "���������", "������", "����������", "����� �������", 1),
    ("����� ����� ������� ���� � ����?", "21 �����", "21 ����", "21 ��������", "21 �������", 2),
    ("����� ����� �������� ����� � ����?", "������", "�������", "����", "������", 2)
]

# ������������ �������
random.shuffle(questions)

# ������������� Pygame
pygame.init()

# �������� ���� Tkinter
root = tk.Tk()
root.title("���������")

# ����������
current_question = 0
score = 0

# ������� ��� �������� ������
def check_answer(selected):
    global current_question, score
    if selected == questions[current_question][5]:
        score += 1
    current_question += 1
    if current_question < 3:
        show_question()
    else:
        messagebox.showinfo("���������", f"�� �������� ��������� �� {score} �� 3 ��������.")
        root.destroy()

# ������� ��� ����������� �������
def show_question():
    question_label.config(text=questions[current_question][0])
    btn1.config(text=questions[current_question][1], command=lambda: check_answer(1))
    btn2.config(text=questions[current_question][2], command=lambda: check_answer(2))
    btn3.config(text=questions[current_question][3], command=lambda: check_answer(3))
    btn4.config(text=questions[current_question][4], command=lambda: check_answer(4))

# ������� Tkinter
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack(pady=20)

btn1 = tk.Button(root, text="", font=("Arial", 14), width=20)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="", font=("Arial", 14), width=20)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="", font=("Arial", 14), width=20)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="", font=("Arial", 14), width=20)
btn4.pack(pady=5)

# ������ ������ �������
show_question()

# ������ Tkinter
root.mainloop()
