import pygame.font
print(pygame.font.get_fonts())
class Buttom():
    """Класс для создания кнопок"""
    def __init__(self, screen):
        pygame.font.init()
        msg = "Играть"
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.height, self.width = 70, 250
        self.buttom_color = (0, 0, 0)
        self.text_color = (255, 255, 0)
        self.path = pygame.font.match_font('arialblack')
        self.font = pygame.font.Font(self.path, 50)
        self.rect = pygame.Rect(0,0, self.width, self.height,)
        self.rect.center = self.screen_rect.center
        self.message_output(msg)

    def message_output(self, msg):
        self.image_msg = self.font.render(msg, True, self.text_color, self.buttom_color)
        self.image_msg_rect = self.image_msg.get_rect()
        self.image_msg_rect.center = self.rect.center

    def draw_buttom(self):
        self.screen.fill(self.buttom_color, self.rect)
        self.screen.blit(self.image_msg, self.image_msg_rect)