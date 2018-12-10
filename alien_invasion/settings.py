class Settings:
    """存储《外星人入侵》的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (200,200,255)
        #飞船移动速度
        # self.ship_speed_factor = 1
        self.ship_limit = 1
        #外星人移动速度
        # self.alien_speed_factor = 1
        #外星人下降速度
        self.fleet_drop_speed = 8

        #子弹初始化
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        # self.bullet_speed_factor = 0.5
        self.bullets_allowed = 5

        #以什么样的速度加快游戏的节奏
        self.speedup_scale = 2
        #加速时外星人分值的加速倍数
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """动态初始化游戏的移动速度"""
        self.ship_speed_factor = 1
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 2

        self.alien_points = 10

        # 标记外星人的移动方向：1表示向右-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        #速度加倍时也初始化外星人的分值
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


