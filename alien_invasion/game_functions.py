import sys,time
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,stats,screen,ship,aliens,bullets,sb):
    """响应按键"""
    # print(event.key)
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings,stats,screen,ship,aliens,bullets,sb)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
def check_events(ai_settings,screen,stats,play_button,aliens,ship,bullets,sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,stats,screen,ship,aliens,bullets,sb)
            # if event.key == pygame.K_RIGHT:
            #     #向右移动飞船
            #     # ship.rect.centerx += 1
            #     ship.moving_right = True
            # if event.key == pygame.K_LEFT:
            #     ship.moving_left = True
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # if event.key == pygame.K_LEFT:
            #     ship.moving_left = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,aliens,ship,bullets,sb,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,aliens,ship,bullets,sb,mouse_x,mouse_y):
    """在玩家单机Play按钮时开始游戏"""
    # print(play_button.rect.collidepoint(mouse_x,mouse_y))
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        # print(stats.score)
        start_game(ai_settings,stats,screen,ship,aliens,bullets,sb)
    #if play_button.rect.collidepoint(mouse_x,mouse_y):
    #     #隐藏光标
    #     pygame.mouse.set_visible(False)
    #     #重置游戏统计信息
    #     stats.reset_stats()
    #     stats.game_active = True
    #     #清空外星人列表和子弹列表
    #     aliens.empty()
    #     bullets.empty()
    #     #创建新的外星人群组，并让飞船居中
    #     create_fleet(ai_settings,screen,ship,aliens)
    #     ship.center_ship()

def start_game(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """开始游戏"""
    #重置游戏设置
    ai_settings.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏统计信息
    stats.reset_stats()
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()
    stats.game_active = True
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()
    # 创建新的外星人群组，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb):
    """更新屏幕上的图像，并且换到新屏幕"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # sb.prep_score()
    sb.show_score()
    sb.prep_gameover()
    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active and stats.ships_left >= 0:
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,bullets,aliens,stats,sb):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中了外星人，如果有就删除他们
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    # print(collisions.values())
    #计分
    for alien in collisions.values():
        stats.score += ai_settings.alien_points * len(alien)
        sb.prep_score()
        # sb.prep_high_score()
        check_high_score(stats,sb)
    #外星人都被消灭之后用新的速度重新创建一批外星人
    if len(aliens) == 0:
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()
# def update_aliens(aliens):
#     """更新外星人位置"""
#     aliens.update()

def fire_bullet(ai_settings,screen,ship,bullets):
    """发射子弹"""
    # 创建一颗子弹，并将其放到bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

# def create_fleet(ai_settings,screen,aliens):
#     """创建外星人群"""
#     #创建一个外星人，并计算一行可以容纳所少个外星人
#     #外星人的间距为外星人的宽度
#     alien = Alien(ai_settings,screen)
#     alien_width = alien.rect.width
#     available_space_x = ai_settings.screen_width - 2 * alien_width
#     number_aliens_x = int(available_space_x / (2 * alien_width))
#
#     # 创建第一行外星人
#     for alien_number in range(number_aliens_x):
#         #创建一个外星人并加入当前行
#         alien = Alien(ai_settings,screen)
#         alien.x = alien_width + 2*alien_width*alien_number
#         print(alien.x)
#         alien.rect.x = alien.x
#         aliens.add(alien)
def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_sapce_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_sapce_y/(2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人，并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # alien.rect.y = 300
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人群"""
    #创建有个外星人，并计算出每行可以容纳多少个外星人
    if len(aliens) == 0:
        alien = Alien(ai_settings,screen)
        num_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
        number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
        #创建第几行外星人-创建第一行外星人（循环嵌套）
        for row_number in range(number_rows):
            for alien_number in range(num_aliens_x):
                create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """响应外星人撞到飞船"""
    #将ships_left减1
    if stats.ships_left > 0:
        sb.prep_ships()
        stats.ships_left -= 1
        #清空现有的外星人以及子弹列表
        aliens.empty()
        bullets.empty()
        pygame.mouse.set_visible(False)
        stats.game_active = False

        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        time.sleep(0.5)
        print(stats.ships_left)
    elif stats.ships_left == 0:
        aliens.empty()
        bullets.empty()
        stats.game_active = True
        sb.prep_gameover()
        # stats.game_active = False
        # pygame.mouse.set_visible(True)




def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
    """检查是否有外星人位于屏幕的边缘，并更新外星人的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    for alien in aliens.copy():
        if alien.rect.top >= ai_settings.screen_height:
            aliens.remove(alien)

    #检测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
        # print("Ship hit!!!")
            # print(len(aliens.copy()))
    # if len(aliens.copy()) < 0:
    #     create_fleet(ai_settings, screen, ship, aliens)

def check_high_score(stats,sb):
    """检查是否诞生了最高分"""
    # print(stats.score)
    # print(stats.high_score)
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()