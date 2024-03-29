import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(pygame.sprite.Sprite):
    """Класс созадающий пришельца"""
    def __init__(self, screen, ai_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.ai_settings = Settings()
        self.image = pygame.image.load('image/противник 1.bmp')
        self.image.set_colorkey(self.ai_settings.alien_bg_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = self.ai_settings.alien_speed_factor
    def update(self):
        """Обнавляет позицию иноплонетянина"""
        self.x += self.speed
        self.rect.x = self.x

        if self.rect.left <= 0 or self.rect.right >= 800:
            self.speed = -self.speed
            if self.rect.left <= 0 or self.rect.right >= 800:
                self.rect.y += self.ai_settings.alien_speed_factor_y


    def blit_alien(self):
        """Рисует иноплонитянина """
        self.screen.blit(self.image_alien, self.rect_alien)

