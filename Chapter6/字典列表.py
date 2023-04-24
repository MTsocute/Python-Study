aliens = []  # 字典列表

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 修改前三只的属性
for alien in aliens[:3]:
    alien['color'] = 'white'
    alien['point'] = 15
    alien['speed'] = 'medium'

# 显示前五个外星人
for alien in aliens[:6]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
