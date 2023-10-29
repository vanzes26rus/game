import pygame.font

class Buttom():
    """Класс для создания кнопок"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("image/старт.bmp")
        self.image = pygame.transform.scale(self.image, (200, 80))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 250
        # фон окна
        self.becgraund = pygame.image.load('image/becgraund.jpg')
        self.becgraund = pygame.transform.scale(self.becgraund, (800, 600))

    def draw_buttom(self):
        self.screen.blit(self.becgraund, (0, 0))
        self.screen.blit(self.image, self.rect)