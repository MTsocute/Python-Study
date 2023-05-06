import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
squares = [1, 4, 25, 49, 81]

# 如此一来坐标就会是输入值和输出值构成的了
plt.plot(input_value, squares, linewidth='3')    # 折线图

# 添加标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()