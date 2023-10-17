import pygame
import sys
import game_fanchen as g_f
from pygame.sprite import Group

from settings import Settings
ai_settings = Settings()
from ship import Ship
from bullet import Bullet



screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption('Очередная попытка')
ship = Ship(screen, ai_settings)
bullets = Group()
aliens = Group()
g_f.create_fleet(ai_settings, screen, aliens, ship)

def start_game():
    pygame.init()
    while True:
        g_f.chek_event(ship, bullets, ai_settings, screen)
        g_f.update_screen(screen, ship, ai_settings, bullets, aliens)

def start_game_2():
    pygame.init()
    while True:
        g_f.chek_event(ship, bullets, ai_settings, screen)
        g_f.update_screen(screen, ship, ai_settings, bullets, aliens)

start_game()