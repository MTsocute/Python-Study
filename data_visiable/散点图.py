import matplotlib.pyplot as plt

# s = size
# plt.scatter(2, 4, s=200)   # 绘制点个点（x,y）

def scatter_demo():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]

    plt.scatter(x_values, y_values,s=100)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    # major: 标尺不会很细，刻度间隙会粗略些
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

def scatter_demo_2():
    x_val = list(range(1, 1001))
    y_val = [pow(x,2) for x in x_val]   # 所有的点都是 x 的平方倍

    plt.figure(figsize=(10, 6))  # 设置图表大小

    plt.scatter(x_val, y_val, s=10)

    # 设置坐标轴的取值范围
    plt.axis(
        [0,1100,    # x 轴
        0,1.1e6]    # y 轴
    )


    plt.show()

if __name__ == '__main__':
    # scatter_demo()
    scatter_demo_2()