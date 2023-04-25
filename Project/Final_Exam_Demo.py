import random


# 快速排序，实现对数据的分类，同时支持用户输入数据来决定升序(0)还是降序(1)
def quick_sort(data, reverse=False):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = []
    right = []

    for i in range(1, len(data)):
        if data[i] <= pivot:
            left.append(data[i])
        else:
            right.append(data[i])

    if reverse:
        return quick_sort(right, reverse=True) + [pivot] + quick_sort(left, reverse=True)
    else:
        return quick_sort(left) + [pivot] + quick_sort(right)


# 用户界面
def Str_UI():
    print("请选择您需要的操作：")
    print("1. 统计数据的最大值、最小值、平均值")
    print("2. 添加数据")
    print("3. 插入数据")
    print("4. 删除数据")
    print("5. 排序")
    print("6. 查找特定值个数")
    print("7. 退出程序")
    print("-" * 40)


# 数据分析主体部分
def data_analysis(Data_Fin):
    while True:
        Str_UI()  # 用户操作提示界面
        choice = input("请输入操作编号：")  # 根据用户输入来判断进行什么操作

        # 统计基础数据
        if choice == "1":
            print("-" * 40)
            print("最大值：", max(Data_Fin))
            print("最小值：", min(Data_Fin))
            print("平均值：", sum(Data_Fin) / len(Data_Fin))
            print("-" * 40)

        # 在列表最后位置添加内容
        elif choice == "2":
            print("-" * 40)
            value = input("请输入需要添加的数据：")
            try:
                Data_Fin.append(int(value))
                print(f'{value} 已添加')
                print("添加后的数据为：", Data_Fin)
            except ValueError:
                print('输入不合法，请输入数字')
            print("-" * 40)

        # 在列表中指定位置插入元素
        elif choice == "3":
            print("-" * 40)
            # 检测用户输入数据，防止乱输入造成影响
            while True:
                try:
                    index = int(input("请输入需要插入的位置（0～9）之间任意数字："))
                    if index >= int(len(Data_Fin)):
                        print("你所输入的数字大于列表的长度，请输入 0～9 中任意一个数字")
                    else:
                        break
                except ValueError:
                    print("输入有误，请检查输入！")
            while True:
                try:
                    value = int(input("请输入需要插入的数据："))
                    break
                except ValueError:
                    print("输入有误，请检查输入！")

            Data_Fin.insert(index, value)
            print("插入后的数据为：", Data_Fin)
            print("-" * 40)

        # 删除列表中的指定元素
        elif choice == "4":
            print("-" * 40)
            value = input("请输入需要删除的数据：")
            try:
                Data_Fin.remove(int(value))
                print(f'{value} 已删除')
            except ValueError:
                print('该内容可能不存在与列表当中')
            print("-" * 40)

        # 实现对表哥内容排序
        elif choice == "5":
            print("-" * 40)
            print("排序前：", Data_Fin)  # 显示未排序前的序列
            # 用户输入0表示升序排列，1表示降序排列，用户乱输入就默认升序
            reverse = input("请选择排序方式（0表示升序，1表示降序）：")
            if reverse == "1":
                print("排序结果：", quick_sort(Data_Fin, reverse=True))
            else:
                print("排序结果：", quick_sort(Data_Fin))
            print("-" * 40)

        # 查找特定值个数
        elif choice == "6":
            while True:
                try:
                    num = int(input('请输入要统计的特定值: '))
                    count = data.count(num)
                    print(f'{num}出现的次数为: {count}')
                    break
                except ValueError:
                    print("输入有误，请重新输入！")

        # 退出程序
        elif choice == "7":
            print("程序已退出！")
            print("-" * 40)
            break

        # 防止用户乱输入
        else:
            print("输入有误，请重新输入！")


# 主函数
def main():
    print("-" * 40)
    print("当前数据为：", data)  # 显示生成的数据内容
    print("-" * 40)
    data_analysis(data)


# 接口
if __name__ == '__main__':
    data = [round(random.uniform(5.0, 20.0), 2) for i in range(10)]  # 随机生成10个股票价格数据
    main()
