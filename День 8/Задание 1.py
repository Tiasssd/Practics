# -*- coding: 1251 -*-
import pygame
import tkinter as tk
from tkinter import Canvas
import random
import math

# ������������� Pygame
pygame.init()

# ��������� ����
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("�������� � ����")

# �����
WHITE = (255, 255, 255)

# �������� �������
background_texture = pygame.image.load("background_texture.png")  # �������� �������� ����
bubble_texture = pygame.image.load("bubble_texture.png")  # �������� �������� �������� � �������������

# ����� ��������
class Bubble:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.texture = bubble_texture

    def move(self):
        self.y -= self.speed
        self.x += math.sin(self.y / 20) * 2  # ��������� ����������

        # ���������� ������� ����� � �����������
        if self.y < HEIGHT / 2:
            self.size += 0.3

    def draw(self):
        scaled_texture = pygame.transform.scale(self.texture, (int(self.size), int(self.size)))
        screen.blit(scaled_texture, (self.x, self.y))

# �������� ���������
bubbles = [Bubble(random.randint(0, WIDTH), random.randint(HEIGHT, HEIGHT + 100), random.randint(20, 40), random.uniform(1, 3)) for _ in range(20)]

# �������� ����
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_texture, (0, 0))  # ��������� �������� ����

    for bubble in bubbles:
        bubble.move()
        bubble.draw()

        # ���������� ��������, ���� �� ����� �� ������� ������
        if bubble.y < -bubble.size:
            bubble.y = random.randint(HEIGHT, HEIGHT + 100)
            bubble.size = random.randint(50, 100)
            bubble.speed = random.uniform(1, 3)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
