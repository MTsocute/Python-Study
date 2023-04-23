# 按照手首字母来排序
alphabet = ['a', 'e', 'c', 'f', 'b']
alphabet.sort() # 排序
print(alphabet)

alphabet.sort(reverse=True) # 逆序
print(alphabet)

print("-"*25 + '\n')

# 临时排序，就是用特定的反思呈现，但是不改变元列表
alphabet2 = ['a', 'e', 'c', 'f', 'b']
print(sorted(alphabet2))
print(alphabet2)
print("-"*25 + '\n')
print(sorted(alphabet2, reverse=True))  # 逆序
print(alphabet2)

print("-"*25 + '\n')

# 反转的输出列表
alphabet3 = ['a', 'e', 'c', 'f', 'b']
alphabet3.reverse() # 逆转列表
print(alphabet3)

# 测量列表的长度
print("The length of the alphabet is "
       + str(len(alphabet)))    # 这里要注意哦，len 是 int 类型的，要转换