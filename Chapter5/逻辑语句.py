print("audi" == "Audi")  # Python == 检测区分大小写

# 多个条件
age = 12
print((age >= 11) and (age <= 100))  # and 多个条件都要满足
print((age >= 11) or (age >= 100))  # or 多个条件都满足一个

# 检测某个关键字在不在列表当中
ls = [1, 23, 4, 5, 6, 7, 8567, 123]
print(1 in ls)  # 1 是否在 ls 当中
print(1 not in ls)  # 1 是否不在 ls 当中
