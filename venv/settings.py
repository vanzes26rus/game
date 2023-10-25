import pygame
class Settings():
    """Класс для хранения настроек игры."""
    def __init__(self,):
        # настройки экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # скорость коробля
        self.speed_ship = 0.8
        self.speed_quantity = 3
        # настройки пули
        self.bullet_speed_factor = 0.125
        self.bullet_bg_color = 255, 255, 255
        self.bullet_maximum = 6
        # Настройки пришельца
        self.alien_bg_color = (255, 255, 255)
        self.alien_speed = 0.03