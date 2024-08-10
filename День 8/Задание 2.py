# -*- coding: 1251 -*-
import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Вопросы и ответы
questions = [
    ("Какой цвет у неба?", "Синий", "Зеленый", "Красный", "Желтый", 1),
    ("Сколько ног у паука?", "6", "8", "10", "12", 2),
    ("Какой самый большой океан?", "Атлантический", "Индийский", "Северный Ледовитый", "Тихий", 4),
    ("Сколько планет в Солнечной системе?", "7", "8", "9", "10", 2),
    ("Какой газ необходим для дыхания?", "Азот", "Кислород", "Водород", "Углекислый газ", 2),
    ("Какой самый высокий водопад в мире?", "Анхель", "Ниагара", "Виктория", "Игуасу", 1),
    ("Какой самый большой континент?", "Африка", "Азия", "Европа", "Антарктида", 2),
    ("Какой самый маленький континент?", "Австралия", "Европа", "Антарктида", "Южная Америка", 1),
    ("Какой самый длинный день в году?", "21 марта", "21 июня", "21 сентября", "21 декабря", 2),
    ("Какой самый короткий месяц в году?", "Январь", "Февраль", "Март", "Апрель", 2)
]

# Перемешиваем вопросы
random.shuffle(questions)

# Инициализация Pygame
pygame.init()

# Создание окна Tkinter
root = tk.Tk()
root.title("Викторина")

# Переменные
current_question = 0
score = 0

# Функция для проверки ответа
def check_answer(selected):
    global current_question, score
    if selected == questions[current_question][5]:
        score += 1
    current_question += 1
    if current_question < 3:
        show_question()
    else:
        messagebox.showinfo("Результат", f"Вы ответили правильно на {score} из 3 вопросов.")
        root.destroy()

# Функция для отображения вопроса
def show_question():
    question_label.config(text=questions[current_question][0])
    btn1.config(text=questions[current_question][1], command=lambda: check_answer(1))
    btn2.config(text=questions[current_question][2], command=lambda: check_answer(2))
    btn3.config(text=questions[current_question][3], command=lambda: check_answer(3))
    btn4.config(text=questions[current_question][4], command=lambda: check_answer(4))

# Виджеты Tkinter
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

# Запуск первой функции
show_question()

# Запуск Tkinter
root.mainloop()
