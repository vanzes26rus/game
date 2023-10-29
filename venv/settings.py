import pygame
class Settings():
    """Класс для хранения настроек игры."""
    def __init__(self):
        # настройки игры
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = pygame.image.load('image/фон.jpg')
        self.bg_color = pygame.transform.scale(self.bg_color, (800, 600))
        # скорость коробля
        # self.speed_ship = 0.8
        self.ship_quantity = 2
        # настройки пули
        # self.bullet_speed_factor = 0.35
        self.bullet_bg_color = 255, 255, 255
        self.bullet_maximum = 3
        # Настройки пришельца
        self.alien_bg_color = (255, 255, 255)
        # self.alien_speed = 1
        self.changeable_setting = 5
        self.alien_speed_factor = 0.3
        self.alien_speed_factor_y = 39
        self.speed_ship = 0.8
        self.bullet_speed_factor = 0.35
    def changeable_settings(self):
        """Изменяемые настройки"""
        self.alien_speed_factor += self.changeable_setting
        self.speed_ship += self.changeable_setting
        self.bullet_speed_factor += self.changeable_setting
        self.alien_speed_factor_y += self.changeable_setting