# 使用一行代码生成一个列表
lnum = [val ** 2 for val in range(1, 11, 2)]
print(lnum)

# 切片
print(lnum[0:2])  # 拿出列表中第一个到第二个元素
print(lnum[:3])  # 没有指定：前数字就默认是开头
print(lnum[2:])  # 没有指定：后数字就默认是结尾
print(lnum[-2:])  # 返回最后两个元素
print(lnum[-4:-2])  # 记住：[:]右边的元素是访问不到的，只能访问到 lnum[-3] 最多

# 列表赋值的问题（C中的浅赋值和深复制问题）
lnum_2 = lnum  # 没有切片，这个会造成两个变量名指向同一个地址，不改变列表
lnum_3 = lnum[:]  # 有切片，创建一个新的列表

lnum_2.append(101)  # 诚然，这个改变回影响 lnum
lnum_3.append(100)  # 这个不会，因为他是独立的一个新列表了

print("The number in lnum = ", lnum)
print("The number in lnum2 = ", lnum_2)
print("The number in lnum3 = ", lnum_3)
