import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('image/ship.bmp')
        self.image.set_colorkey((self.ai_settings.bullet_bg_color))
        self.rect_ship = self.image.get_rect()
        self.rect_screen = self.screen.get_rect()
        self.rect_ship.centerx = self.rect_screen.centerx
        self.rect_ship.bottom = self.rect_screen.bottom
        self.movement_right = False
        self.movement_left = False
        self.center = float(self.rect_screen.centerx)

    def ship_update(self, ai_settings):
        if self.movement_right and self.rect_ship.right < self.rect_screen.right:
            self.rect_ship.centerx += self.ai_settings.speed_ship

        if self.movement_left and self.rect_ship.left > self.rect_screen.left:
            self.rect_ship.centerx -= self.ai_settings.speed_ship
            self.rect_ship.centerx == self.center

    def blit_ship(self):
        self.screen.blit(self.image, self.rect_ship)