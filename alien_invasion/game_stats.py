# from settings import Settings
class GameStats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.high_score = 0
        self.ships_left = self.ai_settings.ship_limit
        self.reset_stats()


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        # self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1



if __name__ == '__main__':
    ai_settings = Settings()
    s = GameStats(ai_settings)
    s.reset_stats()
    print(s.score)