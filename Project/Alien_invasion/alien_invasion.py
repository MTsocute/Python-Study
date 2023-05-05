import pygame
from ship import Ship
import game_function as gf
from setting import Settings
from pygame.sprite import Group
from game_status import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()  # 创建一个基本设置的类对象（包含所需要的参数设置）

    # 创建游戏的窗口，设置大小    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")  # 屏幕的标题

    # 绘制一个飞船对象、一个外星人群、子弹群
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建一个统计游戏信息的对象
    stats = GameStats(ai_settings)

    # 创建外星人舰队
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # 开始游戏的主循环
    while True:
        # 只有游戏活动的时候才可以执行的功能
        if stats.game_active:
            # 子弹的操作(射击、删除)
            gf.update_bullet(bullets)
            # 检测子弹和外星人的撞击
            gf.check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
            # 根据玩家操作控制飞船
            ship.update()
            # 外星人到达底部
            gf.check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
            # 更新外星人动作(是否碰到边界，是否和飞船发生撞击)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)


        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新屏幕内容
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


if __name__ == '__main__':
    run_game()
