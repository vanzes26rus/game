import pygame

class Buttom_exit():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("image/выход.png")
        self.image = pygame.transform.scale(self.image, (200, 80))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
    def blit_buttom_exit(self):
        self.screen.blit(self.image, self.rect)
