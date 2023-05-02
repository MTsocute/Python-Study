import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """ 初始化我们的飞船并放到屏幕中央 """
        self.screen = screen
        self.ai_settings = ai_settings  # 初始化 设置的类对象

        # 加载飞船图像
        self.image = pygame.image.load(
            "/Users/momo/Desktop/Python/Project/Alien_invasion/images/ship.bmp")

        self.rect = self.image.get_rect()  # 让图片变成矩形单位
        self.screen_rect = screen.get_rect()  # 让屏幕变成矩形单位

        # 一开始让飞船出现在屏幕的中央底部
        self.rect.centerx = self.screen_rect.centerx  # 获取屏幕中央位置。传给飞船位置
        self.rect.bottom = self.screen_rect.bottom  # 获取屏幕底部位置。传给飞船位置

        # 利用 center 这个值改变飞船 x 轴位置
        self.centerx = float(self.rect.centerx)  # 使用浮点数，防止整数加法忽略浮点
        self.centery = float(self.rect.centery)  # 使用浮点数，防止整数加法忽略浮点

        # 飞船移动标志
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False


    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据飞船的状态来判断如何移动，注意边界问题 """

        # 向右移动
        if self.move_right and self.rect.right < self.screen_rect.width:
            self.centerx += self.ai_settings.ship_speed
        # 向上移动
        elif self.move_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed
        # 向左移动
        elif self.move_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed
        # 向下移动
        elif self.move_down and self.rect.bottom < self.screen_rect.height:
            self.centery += self.ai_settings.ship_speed


        # 更新飞船的位置
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery