import pygame
from ship import Ship
import game_function as gf
from setting import Settings
from pygame.sprite import Group

def update_bullet(bullets):
    """ 更新子弹位置，删除超出边界的子弹 """
    # 更新子弹的位置，保持向上移动
    bullets.update()

    # 子弹超出顶部，使其消失
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: bullets.remove(bullet)


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()  # 创建一个基本设置的类对象（包含所需要的参数设置）

    # 创建游戏的窗口，设置大小    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")  # 屏幕的标题

    # 绘制一个飞船对象
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 根据玩家操作变动位置
        ship.update()

        # 子弹的操作(射击、删除)
        update_bullet(bullets)

        # 更新屏幕内容
        gf.update_screen(ai_settings, screen, ship, bullets)


if __name__ == '__main__':
    run_game()
