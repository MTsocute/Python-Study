# 我们用字典定义两个外星人，存储了外星人的颜色和对应击败的积分奖励
aline0 = {'color': 'green', 'point': 5}
aline1 = {'color': 'blue', 'point': 10}

print(aline0['color'])  # 让我们来访问其中一个的颜色属性
print(aline1['point'])  # 访问 alien1 的击败奖励积分

# 往空字典中加入属性
aline2 = {}
aline2['color'] = 'cyan'
aline2['point'] = 12
print(aline2)