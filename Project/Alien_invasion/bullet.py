import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ 一个对飞船发射的子弹管理的类 """
    def __init__(self, ai_settings, screen, ship):
        """ 在飞船所在位置创建子弹对象 """
        super().__init__()
        self.screen = screen

        # 在 (0, 0) 创建一个子弹
        self.rect = pygame.Rect(0, 0,
                ai_settings.bullet_width, ai_settings.bullet_height)

        # 调整子弹的位置到船的正上方
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 用小数表示子弹的位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color   # 子弹颜色
        self.speed = ai_settings.bullet_speed   # 子弹速度

    def update(self):
        """ 向上移动子弹 """
        self.y -= self.speed
        self.rect.y = self.y    # 更新子弹实际位置

    def draw_bullet(self):
        """ 在屏幕上绘制子弹 """
        pygame.draw.rect(self.screen, self.color, self.rect)