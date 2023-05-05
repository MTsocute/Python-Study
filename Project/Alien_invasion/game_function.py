import sys
import pygame
import time
from alien import Alien
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

def update_bullet(bullets):
    """ 更新子弹位置，删除超出边界的子弹 """
    # 更新子弹的位置，保持向上移动
    bullets.update()

    # 子弹超出顶部，使其消失
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: bullets.remove(bullet)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """ 响应子弹和外星人的撞击 """
    # 检测是否有子弹打到了外星人，如果是就删除子弹和外星人
    # True 代表删除对象，对应前后顺序
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 如果外星人群消失了
    if len(aliens) == 0:
        # 清空屏幕的所有子弹
        bullets.empty()
        # 再生成新的外星人群
        create_fleet(ai_settings, screen, ship, aliens)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检测外星人是够到达了底部 """
    screen_rect = screen.get_rect()

    # 如果外星人到达了底部，就当飞船被撞处理
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def check_events(ai_settings, screen, ship, bullets):
    """ 监视鼠标和键盘事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击叉叉就是 pygame.Quit 事件发生
            sys.exit()  # 我们用这个函数结束运行
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """ 更新图图到屏幕 """
    screen.fill(ai_settings.bg_color)  # 每次循环都重绘屏幕

    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  # 绘制飞船

    aliens.draw(screen)  # 把Group里面的外星人全部写到屏幕上

    pygame.display.flip()  # 呈现屏幕区域

def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每一行可容纳多少外星人 """
    alien_width = alien_width  # 一个外星人的宽度

    # 除去边界，两个外星人的宽度，就是可以容纳外星人的总长度
    available_space_x = \
        ai_settings.screen_width - 2 * alien_width
    number_aliens_x = \
        int(available_space_x / (2 * alien_width))  # x 轴最多可以出现几个外星人
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """ 计算列可以容纳多少行外星人 """
    available_space_y = \
        (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ 创建一个外星人并放在当前行 """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  # 一个外星人的宽度

    # 每个外星人之间两倍自己的宽度，就相当于是每个外星人之间相距一个外星人的宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x  # 调整外星人位置

    # 每个外星人之间两倍自己的高度，就相当于是每个外星人之间相距一个外星人的高度
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = alien.y

    aliens.add(alien)   # 存入外星人组

def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人舰队 """
    alien = Alien(ai_settings, screen)

    # 行能容纳外星人的数量
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # 列能容纳外星人的数量
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建一屏幕的外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """ 防止外星人撞到边 """
    for alien in aliens.sprites():  # 我们遍历编组的里面的单元
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ 将整群外星人下移，并改变他们的方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
        检测是否外星人在屏幕的边框，然后移动整群外星人的位置
        检测外星人是否和飞船有撞击
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 飞船和外星人发生撞击！
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship Hit!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ 飞船和外星人撞击！ """
    # 生命 -1
    stats.ships_left -= 1

    if stats.ships_left > 0:
        ship.center_ship()
        # 清除屏幕所有外星人和子弹
        aliens.empty()
        bullets.empty()

        # 重新创建一组新的外星人，船放到右下角
        create_fleet(ai_settings, screen, ship, aliens)

        # 暂停下，给玩家反应时间
        time.sleep(1)

    # 如果没有生命了，就结束游戏了
    else:
        stats.game_active = False   # 活动模式关闭