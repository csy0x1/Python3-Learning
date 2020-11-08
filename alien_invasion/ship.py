import pygame

class Ship():
    def __init__(self,ai_settings,screen) -> None:
        #screen决定将飞船绘制到什么位置, 增加ai_settings使飞船可以获取速度设置
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('D:\\Python Project\\alien_invasion\\images\\ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()  #表示屏幕的矩形
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx  #飞船中心的x坐标为屏幕的中心
        self.rect.bottom=self.screen_rect.bottom    #飞船下边缘的y坐标为屏幕的底端
        #以上两条将飞船放置于屏幕底部居中的位置
        self.center=float(self.rect.centerx)    #在飞船的属性centerx中存储小数值
        self.moving_right=False #移动标志
        self.moving_left=False  #移动标志

    def update(self):
        if self.moving_right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center-=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center   #根据self.center更新rect对象

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)