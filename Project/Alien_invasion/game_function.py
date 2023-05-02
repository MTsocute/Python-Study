import sys
import pygame
from bullet import Bullet

def check_keyup_events(event, ship):
    """ 检测是否松开键盘 """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_UP:
        ship.move_up = False
    elif event.key == pygame.K_DOWN:
        ship.move_down = False

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 检测是否按下键盘 """
    # 上下左右移动
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_UP:
        ship.move_up = True
    elif event.key == pygame.K_DOWN:
        ship.move_down = True
    # 空格发射子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)

def fire_bullet(ai_settings, bullets, screen, ship):
    """ 创建子弹对象，并管理发射数量 """
    if len(bullets) < ai_settings.bullet_allow:  # 限制发射子弹数量
        new_bullet = Bullet(ai_settings, screen, ship)  # 创建一颗子弹
        bullets.add(new_bullet) # 添加子弹到编组bullets中


def check_events(ai_settings, screen, ship, bullets):
    """ 监视鼠标和键盘事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击叉叉就是 pygame.Quit 事件发生
            sys.exit()  # 我们用这个函数结束运行
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """ 更新图像，切换到新屏幕 """
    screen.fill(ai_settings.bg_color)  # 每次循环都重绘屏幕

    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # 绘制飞船
    pygame.display.flip()  # 呈现屏幕区域
