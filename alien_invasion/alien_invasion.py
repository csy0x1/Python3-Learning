import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()   #初始化背景设置，让pygame能正常工作
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #创建显示窗口，尺寸为1366*768
    pygame.display.set_caption("Alien_Invasion")

    #bg_color=(128,128,128)    #背景色

    ship=Ship(ai_settings,screen)   #创建飞船

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()