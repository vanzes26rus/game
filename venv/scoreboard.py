import pygame.font
from pygame.sprite import Group
from ship import Ship
pygame.font.init()

class Scoreboard():
    """Класс для вывода счета игры """
    def __init__(self, ai_settings, screen, game_stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_stats = game_stats

    # настройки ширифта для вывода счета
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
    # Подготовка исхлдного изображения.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_lives(self):
        """Выводит оставшиеся количество жизней"""
        levels = int(round(self.ai_settings.ship_quantity))
        levels_str = "Жизни {: }".format(levels)
        self.levels_image = self.font.render(levels_str, True, self.text_color)
        self.levels_rect = self.levels_image.get_rect()
        self.levels_rect.left = self.screen_rect.left
        self.levels_rect.top = self.screen_rect.top + 50

    def prep_level(self):
        """Преобразует число уровня в графическое изображеие"""
        level = int(round(self.game_stats.level))
        level_str = "Уровень {: }".format(level)
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """Преобразует реклрдный счет в графическое изображение"""
        hight_score = int(round(self.game_stats.score, -1))
        hight_score_str = "Рекорд: {:,}".format(hight_score)
        self.hight_score_image = self.font.render(hight_score_str, True, self.text_color)

        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.right = self.screen_rect.right
        self.hight_score_rect.top = self.screen_rect.top


    def prep_score(self):
        """Преобразует текущий счет в изображение."""
        ronder_score = int(round(self.game_stats.score, -1))
        score_str = "Счет: {:,}".format(ronder_score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = self.screen_rect.top + 40

    def show_score(self):
        """Вывод счета на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.levels_image, self.levels_rect)

