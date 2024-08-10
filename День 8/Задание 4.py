# -*- coding: 1251 -*-
import pygame
import random
import threading

# ������������� Pygame
pygame.init()

# ���������
WIDTH, HEIGHT = 800, 600
STAR_COUNT = 20
DISAPPEAR_INTERVAL = 3000  # 5 ������
NEW_STAR_COLOR = (0, 0, 255)  # �����
DISAPPEARING_STAR_COLOR = (255, 165, 0)  # ���������-���������
BACKGROUND_COLOR = (0, 0, 0)  # ������


# ��������� ���� Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("��������� ������")

# ����� ��� ����������� �����
font = pygame.font.SysFont(None, 36)

# ����� ������
class Star:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.max_radius = random.randint(5, 10)
        self.min_radius = random.randint(2, self.max_radius - 2)
        self.radius = self.min_radius
        self.growing = True
        self.speed = random.uniform(0.001, 0.005)
        self.color = (255, 255, 255)
        self.new_star = False
        self.disappearing = False
        self.blackened = False

    def update(self):
        if self.growing:
            self.radius += self.speed
            if self.radius >= self.max_radius:
                self.growing = False
        else:
            self.radius -= self.speed
            if self.radius <= self.min_radius:
                self.growing = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius))

# �������� �����
stars = [Star() for _ in range(STAR_COUNT)]
disappeared_stars = []

# ���������� ��� �������� �����
score = 0

# ������� ��� ���������� �����
def update_stars():
    for star in stars:
        star.update()

# ������� ��� ��������� �����
def draw_stars():
    for star in stars:
        star.draw(screen)

# ������� ��� ����������� �����
def draw_score():
    score_text = font.render(f"����: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# ������� ��� ��������� ������������ � ��������� �����
def manage_stars():
    global score
    while True:
        pygame.time.wait(DISAPPEAR_INTERVAL)
        disappearing_star = random.choice(stars)
        disappearing_star.disappearing = True
        disappearing_star.color = DISAPPEARING_STAR_COLOR
        pygame.time.wait(2000)
        disappearing_star.color = BACKGROUND_COLOR
        disappearing_star.blackened = True
        new_star = Star()
        new_star.new_star = True
        new_star.color = NEW_STAR_COLOR
        stars.append(new_star)
        pygame.time.wait(3000)
        new_star.new_star = False
        new_star.color = (255, 255, 255)
        if disappearing_star in stars:
            stars.remove(disappearing_star)
        disappeared_stars.append((disappearing_star.x, disappearing_star.y))

# ������� ��� ��������� ������ ����
def handle_click(event):
    global score
    x, y = event.pos
    for star in stars:
        if star.x - star.radius <= x <= star.x + star.radius and star.y - star.radius <= y <= star.y + star.radius:
            if star.new_star:
                stars.remove(star)
                score += 1
                return
            elif star.blackened:
                stars.remove(star)
                score += 2
                return
    for (sx, sy) in disappeared_stars:
        if sx - 15 <= x <= sx + 15 and sy - 15 <= y <= sy + 15:
            disappeared_stars.remove((sx, sy))
            score += 2
            return

# ������ ������ ��� ���������� ��������
threading.Thread(target=manage_stars, daemon=True).start()

# �������� ���� ����
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # ���
            handle_click(event)

    screen.fill(BACKGROUND_COLOR)
    update_stars()
    draw_stars()
    draw_score()
    pygame.display.flip()

pygame.quit()
