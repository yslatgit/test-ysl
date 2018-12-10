#coding:utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((1200,800))--已写入配置文件
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen,direction="up")
    # bg_color = (230,230,230)--已写入配置文件

    #创建一个外星人
    alien = Alien(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人编组,创建外星人群
    aliens = Group()
    # print(len(aliens))
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个与用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    #创建按钮的实例
    play_button = Button(ai_settings,screen,"Play")
    #创建计分板实例
    sb = Scoreboard(ai_settings,screen,stats)
    #开始游戏的循环
    while True:

        #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # gf.create_fleet(ai_settings, screen, ship, aliens)
        gf.check_events(ai_settings,screen,stats,play_button,aliens,ship,bullets,sb)
        #每次循环时都重新绘制屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # #让绘制的屏幕可见
        # pygame.display.flip()
        if stats.game_active:
            ship.update()#监控键盘事件
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb)




if __name__ == '__main__':
    run_game()

