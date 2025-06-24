import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

SQUARE_SIZE = 25

clock = pygame.time.Clock()
SPEED = 15

def draw_square(x, y, color):
    pygame.draw.rect(SCREEN, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

def get_random_x():
    return random.randint(0, (WIDTH // SQUARE_SIZE) - 1) * SQUARE_SIZE

def get_random_y():
    return random.randint(0, (HEIGHT // SQUARE_SIZE) - 1) * SQUARE_SIZE

def get_apple_position():
    apple_position = snake_positions[0]
    while apple_position in snake_positions:
        apple_position = (get_random_x(), get_random_y())

    return apple_position

snake_positions = apple_position = direction = []

def reset_game():
    global snake_positions, apple_position, direction

    snake_positions = [(get_random_x(), get_random_y())]
    apple_position = get_apple_position()
    direction = [0, 0]

reset_game()

in_game = True
while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False
        if event.type == pygame.KEYDOWN:
            k = event.key

            if k == pygame.K_LEFT and direction[0] == 0: direction = [-1, 0]
            elif k == pygame.K_RIGHT and direction[0] == 0: direction = [1, 0]
            elif k == pygame.K_UP and direction[1] == 0: direction = [0, -1]
            elif k == pygame.K_DOWN and direction[1] == 0: direction = [0, 1]
            elif k == pygame.K_ESCAPE: in_game = False

    SCREEN.fill((0, 0, 0))

    new_head_x = snake_positions[0][0] + (direction[0] * SQUARE_SIZE)
    new_head_y = snake_positions[0][1] + (direction[1] * SQUARE_SIZE)

    x_bounds_condition = (0 <= new_head_x <= (WIDTH - SQUARE_SIZE))
    y_bounds_condition = (0 <= new_head_y <= (HEIGHT - SQUARE_SIZE))

    touch_condition = (new_head_x, new_head_y) in snake_positions[:-1]

    if not (x_bounds_condition and y_bounds_condition) or touch_condition:
        reset_game()
        continue

    snake_positions.insert(0, (new_head_x, new_head_y))
    
    if (new_head_x == apple_position[0] and new_head_y == apple_position[1]):
        apple_position = get_apple_position()
    else: 
        snake_positions.pop()
        
    draw_square(apple_position[0], apple_position[1], (255, 0, 0))
    
    for snake_position in snake_positions:
        draw_square(snake_position[0], snake_position[1], (0, 255, 0))

    pygame.display.flip()
    clock.tick(SPEED)

pygame.quit()