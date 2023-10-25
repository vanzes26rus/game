import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
from buttom import Buttom


def check_aliens_bottom(stats, bullets, aliens, ai_settings, screen, ship):
    """Проверяет соприкосновение пришельцев с нижнем краем игрового окна"""
    screen = screen.get_rect()
    for alien in aliens:
        if  alien.rect.bottom >= screen.bottom:
            ship_hit(stats, bullets, aliens, ai_settings, screen, ship)
            break
def ship_hit(stats, bullets, aliens, ai_settings, screen, ship):
    """обнавляет позицию коробля и создает новый флот """
    if stats.ship_quantity > 0:
        stats.ship_quantity -= 1
        print(stats.ship_quantity)
#     очищает группы пуль и пришельцев
        bullets.empty()
        aliens.empty()
#     создает новый флот пришельцев
        create_fleet(ai_settings, screen, aliens, ship)
#   обгавляет позицию корабля по середине экрана
        ship.center_ship()
#   пауза
        sleep(2)
    else:
        stats.activ_game = False

def check_aliens_collisions(bullets, aliens):
    """Обрабатывает колизии пули и пришельцев"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
def fire_bullet(screen, ai_settings, bullets, ship):
    """Инициализирует выстрел пули."""
    if len(bullets) < ai_settings.bullet_maximum:
        new_bullet = Bullet(ai_settings, ship, screen)
        bullets.add(new_bullet)

def update_bullets(bullets, aliens, ai_settings, screen, ship):
    """Вывод пули на экран."""
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        check_aliens_collisions(bullets, aliens)
        if len(aliens) == 0:
            bullets.empty()
            create_fleet(ai_settings, screen, aliens, ship)
def remove_bullets(bullets):
    """Удаление старых пуль на экране."""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def chek_keydown(event, ship, bullets, ai_settings, screen):
    # if event.key == pygame.K_UP:
    #     ship.rect.centery -= 50
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


def update_aliens(stats, bullets, aliens, ai_settings, screen, ship):
    """Обнавляет позицию энопланетян"""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Вы проиграли")
        ship_hit(stats, bullets, aliens, ai_settings, screen, ship)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Опредиляет количество рядов пришельцев."""
    # Количество доступных рядов
    available_space_y = ai_settings.screen_height - 2 * ship_height - 4 * alien_height
    # Количество доступных строк
    number_rows = int(available_space_y / alien_height)
    return number_rows


def get_number_aliens_x(ai_settings, alien_widht):
    available_space_x = ai_settings.screen_width - (4 * alien_widht)
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
    number_rows = int(get_number_rows(ai_settings, ship.rect.height, alien.rect.height))

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



def update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_buttom):
    screen.fill(ai_settings.bg_color)
    update_bullets(bullets, aliens, ai_settings, screen, ship)
    bullets.update()

    if stats.activ_game:
        # Проверяет количество жизней
        update_aliens(stats, bullets, aliens, ai_settings, screen, ship)

    check_aliens_bottom(stats, bullets, aliens, ai_settings, screen, ship)
    remove_bullets(bullets)
    ship.blit_ship()
    aliens.draw(screen)
    ship.ship_update(ai_settings)

    if not stats.activ_game:
        play_buttom.draw_buttom()
    pygame.display.flip()


