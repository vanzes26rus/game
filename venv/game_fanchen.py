import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
from buttom import Buttom
from buttum_exit import Buttom_exit
a = Alien(screen, ai_settings)

def check_aliens_bottom(stats, bullets, aliens, ai_settings, screen, ship):
    """Проверяет соприкосновение пришельцев с нижнем краем игрового окна"""
    screen = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen.bottom:
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
        sleep(1)
    else:
        stats.activ_game = False
        pygame.mouse.set_visible(True)

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
            ai_settings.changeable_settings()

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


def chek_event(ship, bullets, ai_settings, screen, stats, play_buttom, aliens, exit_buttom):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                chek_keydown(event, ship, bullets, ai_settings, screen)

            elif event.type == pygame.KEYUP:
                check_keyup(event, ship)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                """события мыши"""
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_buttom(mouse_x, mouse_y, stats, play_buttom, aliens, bullets, ship, ai_settings, screen)
                # кнопка выхода из игры
                check_exit_buttom(mouse_x, mouse_y, exit_buttom, stats)


def check_exit_buttom(mouse_x, mouse_y, exit_buttom, stats):
    """Функция кнопки выхода из игры"""
    c = exit_buttom.rect.collidepoint(mouse_x, mouse_y)
    if c and not stats.activ_game:
        sys.exit()
def check_play_buttom(mouse_x, mouse_y, stats, play_buttom, aliens, bullets, ship, ai_settings, screen):
    """Проверяет нажатия мыши на кнопку играть"""
    buttom_cleced = play_buttom.rect.collidepoint(mouse_x, mouse_y)
    if buttom_cleced and not stats.activ_game:
        # ai_settings.settings_game()
        pygame.mouse.set_visible(False)
        stats.stats_reset()
        stats.activ_game = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()


def update_aliens(stats, bullets, aliens, ai_settings, screen, ship):
    """Обнавляет позицию энопланетян"""
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Вы проиграли")
        ship_hit(stats, bullets, aliens, ai_settings, screen, ship)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Опредиляет количество рядов пришельцев."""
    # Количество доступных рядов
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height

    # Количество доступных строк
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_widht):
    available_space_x = ai_settings.screen_width - (4 * alien_widht)
    number_aliens_x = int(available_space_x / alien_widht)
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_widht = alien.rect.width
    alien.x = alien_widht + 1.3 * alien_widht * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height +  1.5 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """Создает флот пришеьцев."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = int(get_number_rows(ai_settings, ship.rect.height, alien.rect.height))

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



def update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_buttom, exit_buttom):
    screen.blit(ai_settings.bg_color, (0,0))

    if stats.activ_game:
        # Проверяет количество жизней
        update_aliens(stats, bullets, aliens, ai_settings, screen, ship)

    update_bullets(bullets, aliens, ai_settings, screen, ship)
    ship.blit_ship()
    aliens.draw(screen)
    bullets.update()
    check_aliens_bottom(stats, bullets, aliens, ai_settings, screen, ship)
    remove_bullets(bullets)
    ship.ship_update(ai_settings)

    if  stats.activ_game == False:
        play_buttom.draw_buttom()
        exit_buttom.blit_buttom_exit()

    pygame.display.flip()


