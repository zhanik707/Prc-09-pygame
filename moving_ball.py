import pygame
import sys

pygame.init()

# размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# позиция шара
x, y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # управление стрелками
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x - speed - radius >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + speed + radius <= WIDTH:
                x += speed
            if event.key == pygame.K_UP and y - speed - radius >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + speed + radius <= HEIGHT:
                y += speed

    # фон
    screen.fill((255, 255, 255))

    # рисуем шар
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.update()
    clock.tick(60)