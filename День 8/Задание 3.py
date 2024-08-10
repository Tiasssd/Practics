 # -*- coding: 1251 -*-
import pygame
import sys
import random
import math

# Инициализация Pygame
pygame.init()

# Окно игры
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("City Bloxx")
clock = pygame.time.Clock()

# Цвета
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Блоки (этажи)
block_width, block_height = 50, 20

# Позиция блока
block_x, block_y = 350, 100

# Позиция крана
crane_x = screen_width // 2
crane_width, crane_height = 10, 100
crane_color = red

# Скорость движения
crane_speed = 2
block_speed = 3

# Флаг для сброса блока
block_dropping = False

# Список для хранения блоков башни
tower_blocks = [(299, 580, (0,0,0))]
print(len(tower_blocks))

frame_count = 0
frame_rate = 75
interval = 2
counter = 0
counter1 = 0
counter2 = 0
counter_blocks_for_all_time = 1

tower_swing_angle = 0
swing_amplitude = 0

# Главный цикл игры
while True:
    tower_swing_angle += 0.01
    counter2 = 0
    if counter1 == 0:
        fall_block_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        counter1 += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not block_dropping:
                block_dropping = True

    # Движение крана
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        crane_x -= crane_speed
    elif keys[pygame.K_RIGHT]:
        crane_x += crane_speed

    # Ограничение движения крана
    crane_x = max(0, min(crane_x, screen_width - crane_width))
    
    if len(tower_blocks) > 15:
       del tower_blocks[0]
       counter += 1
       for i, (bx, by, color) in enumerate(tower_blocks):
           tower_blocks[i] = (bx, by + 21, color)
           
    if len(tower_blocks) % 5 == 0:
        interval *= 0.75 
    
    # Движение блока
    if block_dropping:
        block_y += block_speed
        if block_y >= screen_height:
            print("Game Over")
            pygame.quit()
            sys.exit()
        if len(tower_blocks) == 1:
            if block_y == 580 - block_height - 1 and block_x >= 275 and block_x <= 525:
                block_dropping = False
                new_block = (block_x, block_y, fall_block_color)
                tower_blocks.append(new_block)
                block_x, block_y = crane_x + crane_width // 2 - block_width // 2, 100
                counter1 -= 1
                counter_blocks_for_all_time += 1
        else:
            bx, by, color = tower_blocks[-1]
            if block_y == by - block_height - 1 and block_x <= int(bx + (block_width) + (block_width * 0.5)) and block_x >= int(bx - (block_width * 0.5)):
                block_dropping = False
                new_block = (block_x, block_y, fall_block_color)
                tower_blocks.append(new_block)
                block_x, block_y = crane_x + crane_width // 2 - block_width // 2, 100
                counter1 -= 1
                counter_blocks_for_all_time += 1
    else:
        block_x = crane_x + crane_width // 2 - block_width // 2
        
    if len(tower_blocks) % 7 == 0:
        swing_amplitude = 0.0001 + (0.007 * counter_blocks_for_all_time)
    swing_offset = swing_amplitude * math.sin(tower_swing_angle)
    for i, (bx, by, color) in enumerate(tower_blocks):
        tower_blocks[i] = (bx + swing_offset,by,color)

    # Отрисовка блока, крана и башни
    screen.fill(white)
    if counter == 0:
         for i, (bx, by, color) in enumerate(tower_blocks):
             if i == 0:       
                    pygame.draw.rect(screen, color, (bx, by, 200, 20))
             else:
                    pygame.draw.rect(screen, color, (bx ,by , block_width, block_height))
    else:
        for i, (bx, by, color) in enumerate(tower_blocks):
            pygame.draw.rect(screen, color, (bx, by, block_width, block_height))
    pygame.draw.rect(screen, fall_block_color, (block_x, block_y, block_width, block_height))
    pygame.draw.rect(screen, crane_color, (crane_x, 0, crane_width, crane_height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Количетсво этажей: {counter_blocks_for_all_time - 1}", True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))




    pygame.display.flip()
    clock.tick(frame_rate)

# Завершение игры
pygame.quit()
sys.exit()

