import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
RED = (213, 50, 80)

# Clock to control game speed
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont('Poppins', 35)

# Snake settings
snake_speed = 10
snake_block = BLOCK_SIZE
snake = []
snake_length = 1

# Initial position and direction
x = WIDTH // 2
y = HEIGHT // 2
dx = 0
dy = 0

# Food position
food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

# Score
score = 0
high_score = 0

def draw_snake(snake_list):
    for part in snake_list:
        pygame.draw.rect(screen, BLACK, [part[0], part[1], BLOCK_SIZE, BLOCK_SIZE])

def draw_food(x, y):
    pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

def show_score():
    value = font.render(f"Score: {score} High Score: {high_score}", True, BLACK)
    screen.blit(value, [0, 0])

# Main game loop
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx = -BLOCK_SIZE
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = BLOCK_SIZE
                dy = 0
            elif event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -BLOCK_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = BLOCK_SIZE

    if game_over:
        screen.fill(RED)
        message = font.render("Game Over", True, BLACK)
        screen.blit(message, [WIDTH // 4, HEIGHT // 2])
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    # Update snake position
    x += dx
    y += dy

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        game_over = True

    # Snake growing
    snake.append([x, y])
    if len(snake) > snake_length:
        del snake[0]

    # Check for self-collision
    for segment in snake[:-1]:
        if segment == [x, y]:
            game_over = True

    # Check for food collision
    if x == food_x and y == food_y:
        score += 4
        food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        snake_length += 1
        if score > high_score:
            high_score = score

    # Drawing everything
    screen.fill(BLUE)
    draw_food(food_x, food_y)
    draw_snake(snake)
    show_score()

    # Refresh screen
    pygame.display.update()

    # Control speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
