import pygame
import datetime
import os

# 1. Инициализация
pygame.init()
WIDTH, HEIGHT = 800, 800 # Размер окна под циферблат
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Transparent Clock")
clock = pygame.time.Clock()

# Настройка путей
current_path = os.path.dirname(__file__) 
images_path = os.path.join(current_path, 'images')

# 2. Загрузка и подготовка картинок
try:
    # Загружаем фон
    bg = pygame.image.load(os.path.join(images_path, "main-clock.png")).convert()
    
    # Загружаем руки с прозрачностью (convert_alpha())
    left_hand_raw = pygame.image.load(os.path.join(images_path, "left-hand.png")).convert_alpha()
    right_hand_raw = pygame.image.load(os.path.join(images_path, "right-hand.png")).convert_alpha()

    # Получаем исходные размеры
    s_w, s_h = left_hand_raw.get_size()
    m_w, m_h = right_hand_raw.get_size()

    # Например, делаем ширину в 0.3 от оригинала, а длину в 0.8
    new_sec_w, new_sec_h = int(s_w * 0.3), int(s_h * 0.8)
    new_min_w, new_min_h = int(m_w * 0.4), int(m_h * 0.7)

    # Применяем масштаб
    left_hand = pygame.transform.smoothscale(left_hand_raw, (new_sec_w, new_sec_h))
    right_hand = pygame.transform.smoothscale(right_hand_raw, (new_min_w, new_min_h))

except pygame.error as e:
    print(f"Ошибка загрузки: {e}")
    pygame.quit()
    exit()

def rotate_hand(surface, angle):
    """Вращает руку вокруг центра экрана"""
    # -angle, т.к. pygame вращает против часовой стрелки
    rotated_surface = pygame.transform.rotate(surface, -angle)
    # Сохраняем центр вращения в центре экрана
    rect = rotated_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    return rotated_surface, rect

# 3. Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.datetime.now()
    # Угол: 1 деление (секунда/минута) = 6 градусов
    sec_angle = now.second * 6
    min_angle = now.minute * 6

    # --- Отрисовка ---
    # Сначала фон (циферблат)
    screen.blit(bg, (0, 0))

    # Рисуем правую руку (Минуты) — она должна быть под секундной
    m_img, m_rect = rotate_hand(right_hand, min_angle)
    screen.blit(m_img, m_rect)

    # Рисуем левую руку (Секунды) — она сверху
    s_img, s_rect = rotate_hand(left_hand, sec_angle)
    screen.blit(s_img, s_rect)

    pygame.display.flip()
    clock.tick(25) # Чуть быстрее для плавности секундной руки

pygame.quit()