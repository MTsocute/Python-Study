from die import Die

# 创建一个六面骰子
die = Die()

results = []

for roll_num in range(100):
    results.append(die.roll())

print(results)

# 分析各个点数出现的频率
frequency = []

for i in range(1, die.num_sides + 1):
    frequency.append(results.count(i))

print(frequency)
