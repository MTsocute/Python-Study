import random

"""
    random.choice([a, b, c])：从列表中任选一个返回
"""


class RandomWalk:
    """ 随机生成漫步数据的类 """

    def __init__(self, num_points=5000):
        """ 初始化随机漫步属性 """
        self.num_points = num_points  # 记录点的数量
        # 所有随机数据起始于 (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 生成随机漫步的所有点 """
        # 在到达指定步数前不停止
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()

            # 以免原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一点的 x 和 y 的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """ 生成每一步 """
        # 决定前景的方向(左右)
        x_direction = random.choice([1, -1])
        y_direction = random.choice([1, -1])

        # 沿这个方向前进的距离(上下)
        x_distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        # 实现前进的方向和距离
        x_step = x_direction * x_distance
        y_step = y_direction * y_distance

        return x_step, y_step


if __name__ == '__main__':
    rw = RandomWalk()
    rw.fill_walk()
    print(rw.x_values)
