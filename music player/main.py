import pygame
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Music Player")

player = MusicPlayer()
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

running = True

while running:
    screen.fill((255, 255, 255))

    # ОБЯЗАТЕЛЬНО события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # КЛАВИШИ (самый стабильный способ!)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.prev()

            elif event.key == pygame.K_q:
                running = False

    # текст
    text = font.render(player.get_current_track(), True, (0, 0, 0))
    screen.blit(text, (20, 80))

    pygame.display.update()
    clock.tick(30)

pygame.quit()