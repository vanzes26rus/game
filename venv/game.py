import pygame
import sys
import game_fanchen as g_f
from pygame.sprite import Group

from settings import Settings
ai_settings = Settings()
from ship import Ship
from bullet import Bullet
from game_stats import Game_Stas
from buttom import Buttom
from buttum_exit import Buttom_exit

screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Очередная попытка №5')
stats = Game_Stas(ai_settings)
ship = Ship(screen, ai_settings)
bullets = Group()
aliens = Group()
play_buttom = Buttom(screen)
exit_buttom = Buttom_exit(screen)
g_f.create_fleet(ai_settings, screen, aliens, ship)

def start_game():
    pygame.init()
    while True:
        g_f.chek_event(ship, bullets, ai_settings, screen, stats, play_buttom, aliens, exit_buttom)
        g_f.update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_buttom, exit_buttom)

def start_game_2():
    pygame.init()
    while True:
        g_f.chek_event(ship, bullets, ai_settings, screen, stats, play_buttom, )
        g_f.update_screen(screen, ship, ai_settings, bullets, aliens, stats, play_buttom)

start_game()