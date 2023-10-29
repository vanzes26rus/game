import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для пули"""
    def __init__(self, ai_settings, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("image/пуля.bmp")
        self.image = pygame.transform.scale(self.image, (200, 80))
        self.image.set_colorkey((ai_settings.bullet_bg_color))
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.speed_bullet = self.ai_settings.bullet_speed_factor
        self.bullet_run_y = float(self.rect.y)

    def update(self):
        """Перемещает пулю вверх по экрану"""
        self.bullet_run_y -= self.speed_bullet
        self.rect.y = self.bullet_run_y

    def draw_bullet(self):
        "Выводит пулю на экран."
        self.screen.blit(self.image , self.rect)

