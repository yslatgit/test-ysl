import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """显示得分信息的类"""

    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.game_over_font = pygame.font.SysFont(None,50)

        #准备初始化得分的图像,以及剩余飞船数量的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_gameover()

    def prep_score(self):
        """将得分转化为一幅渲染的图像#1普通样式展示2.千位出现分隔符"""
        # 1.score_str = str(self.stats.score)
        round_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高分转化为一幅渲染图像"""
        high_score = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.ai_settings.bg_color)

        #将得分放在最上方中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """将游戏等级渲染为一幅图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 50


    def prep_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen,"up")
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_gameover(self):
        """游戏结束"""
        game_over = "游戏结束"
        self.game_over_image = self.game_over_font.render(game_over, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在最上方中间
        self.game_over_image_rect = self.game_over_image.get_rect()
        self.game_over_image_rect.centerx = self.screen_rect.centerx
        self.game_over_image_rect.top = 100

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        #绘制飞船
        self.ships.draw(self.screen)