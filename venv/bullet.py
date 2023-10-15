import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для пули"""
    def __init__(self, ai_settings, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings рропро
        self.image = pygame.image.load("image/пуля.bmp")
        self.image.set_colorkey((ai_settings.bullet_bg_color))
        self.rect_bullet = self.image.get_rect()
        self.rect_bullet.centerx = ship.rect_ship.centerx
        self.rect_bullet.top = ship.rect_ship.top

        self.speed_bullet = self.ai_settings.bullet_speed_factor
        self.bullet_run_y = float(self.rect_bullet.y)

    def update(self):
        """Перемещает пулю вверх по экрану"""
        self.bullet_run_y -= self.speed_bullet
        self.rect_bullet.y = self.bullet_run_y

    def draw_bullet(self):
        "Выводит пулю на экран."
        self.screen.blit(self.image , self.rect_bullet)

