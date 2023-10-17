import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(screen, ai_settings, bullets, ship):
    """Инициализирует выстрел пули."""
    if len(bullets) < ai_settings.bullet_maximum:
        new_bullet = Bullet(ai_settings, ship, screen)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Вывод пули на экран."""
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def remove_bullets(bullets):
    """Удаление старых пуль на экране."""
    for bullet in bullets.copy():
        if bullet.rect_bullet.bottom <= 0:
            bullets.remove(bullet)

def chek_keydown(event, ship, bullets, ai_settings, screen):
    if event.key == pygame.K_RIGHT:
        ship.movement_right = True
    if event.key == pygame.K_LEFT:
        ship.movement_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(screen, ai_settings, bullets, ship)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movement_right = False
    if event.key == pygame.K_LEFT:
        ship.movement_left = False


def chek_event(ship, bullets, ai_settings, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                chek_keydown(event, ship, bullets, ai_settings, screen)
            elif event.type == pygame.KEYUP:
                check_keyup(event, ship)


def update_aliens(aliens):
    """Обнавляет позицию энопланетян"""
    aliens.update()

def get_number_rows(ai_settings, ship_height, alien_height):
    """Опредиляет количество рядов пришельцев."""
    # Количество доступных рядов
    available_space_y = ai_settings.screen_height - 2 * ship_height - 4 * alien_height
    # Количество доступных строк
    number_rows = int(available_space_y / alien_height)
    return number_rows


def get_number_aliens_x(ai_settings, alien_widht):
    available_space_x = ai_settings.screen_width - 4 * alien_widht
    number_aliens_x = int(available_space_x / alien_widht)
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_widht = alien.rect.width
    alien.x = alien_widht + alien_widht * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """Создает флот пришеьцев."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = int(get_number_rows(ai_settings, ship.rect_ship.height, alien.rect.height))

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



def update_screen(screen, ship, ai_settings, bullets, aliens):
    screen.fill(ai_settings.bg_color)
    update_bullets(bullets)
    bullets.update()
    update_aliens(aliens)
    remove_bullets(bullets)
    ship.blit_ship()
    aliens.draw(screen)
    ship.ship_update(ai_settings)
    pygame.display.flip()


