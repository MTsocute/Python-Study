# 简单的多选择结构的 if
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:  # 这里 elif 数量不限，所以选择结构还可以更大程度上的分化
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# if 检测列表是够为空
ls = [1, 2, 3]
ls2 = []

if ls:  # 如果里面至少含有一个以上的元素，就会返回 True
    print("Something in it")
else:
    print("Nothing in it")

if ls2:
    print("Something in it")
else:
    print("Nothing in it")


