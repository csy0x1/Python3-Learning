import sys
import pygame

def check_keydown_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True

def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

def check_events(ship):
    #响应按键和鼠标事件
    for event in pygame.event.get():    #监听鼠标和键盘事件
        if event.type==pygame.quit:
            sys.quit()
        
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship)

        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)   #设置背景色
    ship.blitme()
    pygame.display.flip()   #负责更新屏幕