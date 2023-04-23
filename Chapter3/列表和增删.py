bicycles = ['trek', 'cannondale', 'redline', 'specialized']  # 一个列表
print(bicycles)  # 打印列表
print(bicycles[0])  # 范围列表中的第一个元素

print(bicycles[-1])  # 逆序就是从最后一个开始，但是负数 -1 就是第一个

# 搭配的使用
print("I am " + bicycles[-1] + " in " + "finding " + bicycles[2].title())

# 添加元素到末尾
Lnum = [1, 2, 3, 4, 5]
Lnum.append(6)
print(Lnum)

# 插入元素
Lnum.insert(0, 0)   # 第一个位置插入 0，同时其他元素右移
print(Lnum)

# 删除列表指定位置的元素
del Lnum[0]
print(Lnum)
del Lnum[1]
print(Lnum)

# 删除 栈顶元素[屁股的元素]
print(Lnum.pop())   # 如果你是删除的时候打印的话，它回返回它弹出的元素
# 当然它甚至可以被赋值
lastNumber = Lnum.pop()
print("The last number we del is " + str(lastNumber))

# 我们也可以用它来删除指定位置的位置的东东
pp = ["Momo", "MT", "Flower"]
print(pp.pop(1))    # 删除2号位

# 要死知道名字的话，可以 .remove()
pp.remove("Flower")
print(pp)   # remove 只能确保删除一次哈，如果有重复的，那就重复几次
