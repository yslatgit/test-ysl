import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_setting,screen,direction):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.hero_lists = []
        #加载飞船图像并获取其外接矩形
        # self.image = pygame.image.load("images/hero.gif")
        # self.rect = self.image.get_rect()
        # self.image2 = pygame.image.load("images/hero2.png")
        # self.rect2 = self.image2.get_rect()
        self.screen_rect = screen.get_rect()
        

        if direction == "up":
            #将每艘飞船放在屏幕底部中央
            # self.image = pygame.image.load("images/hero.gif")
            self.image = pygame.image.load("images/ship.png")
            self.rect = self.image.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
            self.hero_lists.append((self.image,self.rect))
        if direction == "right":
        # if direction:
            #将每艘飞船放在屏幕左侧中央
            self.image2 = pygame.image.load("images/hero2.png")
            self.rect2 = self.image2.get_rect()
            self.rect2.centery = self.screen_rect.centery
            self.rect2.left = self.screen_rect.left
            self.hero_lists.append((self.image2,self.rect2))

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_setting.ship_speed_factor
        # time.sleep(2)
        # print(self.rect.left, self.rect.right)

    def blitme(self):
        """在指定位置绘制飞船"""
        # for hero in self.hero_lists:
        self.screen.blit(self.image,self.rect)
        # self.screen.blit(self.image2,self.rect2)
        #     self.screen.blit(hero[0],hero[1])

    def center_ship(self):
        """让飞船在屏幕上底部，居中"""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

class BaseShip:

    def __init__(self,ai_settings,screen,type):
        """
        :param ai_settings: 传入设置类的实例
        :param screen:传入画布
        :param type:飞船的类型：1-hero,2-hero2
        """
        pass