import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('image/ship.bmp')
        self.image.set_colorkey((self.ai_settings.bullet_bg_color))
        self.rect = self.image.get_rect()
        self.rect_screen = self.screen.get_rect()
        self.rect.centerx = self.rect_screen.centerx
        self.rect.bottom = self.rect_screen.bottom
        self.movement_right = False
        self.movement_left = False
        self.center = float(self.rect_screen.centerx)

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)
    def ship_update(self, ai_settings):
        if self.movement_right and self.rect.right < self.rect_screen.right:
            self.rect.centerx += self.ai_settings.speed_ship

        if self.movement_left and self.rect.left > self.rect_screen.left:
            self.rect.x -= self.ai_settings.speed_ship
        self.rect.x == self.center
    # def blit_ship(self):
    #     self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """Обнавляет позицию коробля по центру экрана"""
        self.rect.centerx = self.rect_screen.centerx