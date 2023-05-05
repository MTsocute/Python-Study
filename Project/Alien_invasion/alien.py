import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ 表示单个外星人的类 """
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 外星人图像
        self.image = pygame.image.load(
            '/Users/momo/Desktop/Python/Project/Alien_invasion/images/alien.bmp')
        # 变成像素
        self.rect = self.image.get_rect()

        # 每个外星人都生成在左上角生成
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 利用这个x变量，控制使外星人在水平方向出现位置
        self.x = float(self.rect.x)

    def blitme(self):
        """ 在屏幕上绘制外星人 """
        self.screen.blit(self.image, self.rect)


    def update(self):
        """ 向指定方向移动移动外星人 """
        self.x += (self.ai_settings.alien_speed *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ 如何外星人位于屏幕的边框位置就返回 True """
        screen_rect = self.screen.get_rect()
        # 右边
        if self.rect.right >= screen_rect.right:
            return True
        # 左边
        elif self.rect.left <= 0:
            return True