import pygame
import random

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

snake_block = 20
snake_speed = 15

font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def game_loop():
    global snake_speed  

    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    
    powerup_active = False
    powerup_timer = 0
    powerup_x = -1
    powerup_y = -1

   
    score = 0

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message(f"You Lost! Score: {score} Press Q-Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)

        
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])

        
        if not powerup_active and random.randint(1, 100) == 1:
            powerup_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            powerup_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
        
        if powerup_x != -1 and powerup_y != -1:
            pygame.draw.rect(window, BLUE, [powerup_x, powerup_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_list)

        
        score_text = font.render(f"Score: {score}", True, WHITE)
        window.blit(score_text, [0, 0])

        pygame.display.update()

        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 1

        
        if x1 == powerup_x and y1 == powerup_y:
            powerup_active = True
            powerup_timer = pygame.time.get_ticks()
            powerup_x = -1
            powerup_y = -1
            snake_speed += 5

        
        if powerup_active and pygame.time.get_ticks() - powerup_timer > 5000:
            powerup_active = False
            snake_speed -= 5

        clock.tick(snake_speed)

    pygame.quit()
    quit()

while True:
    game_loop()