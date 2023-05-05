class Settings:
    """ 存储《外星人入侵》所有设置的类 """

    def __init__(self):
        """ 初始化游戏设置 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的速度
        self.ship_speed = 1.5
        # 飞船的生命数
        self.ship_limit = 3

        # 外星人移动速度
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        # fleet_direction: 1为右移，-1为左移
        self.fleet_direction = 1

        # 子弹设置
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allow = 4  # 限制屏幕上最多只能出现 10 个子弹