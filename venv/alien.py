import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(pygame.sprite.Sprite):
    """Класс созадающий пришельца"""

    def __init__(self, screen, ai_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = Settings()
        self.image = pygame.image.load('image/противник.bmp')
        self.image.set_colorkey(self.ai_settings.alien_bg_color)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Проверяет достиг достижение края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.alien_speed_direchions
        self.rect.x = self.x

    def blit_alien(self):
        self.screen.blit(self.image_alien, self.rect_alien)

