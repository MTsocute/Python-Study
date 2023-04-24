aline0 = {'color': 'green', 'point': 5}
print("Aline0's attributes used to be ", aline0)

# 修改字典中的属性
aline0['color'] = 'bugyellow'
print("Aline0's attributes are ", aline0)

del aline0['color']  # 删除字典某一个属性
print(aline0)

# 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():  # 可以用两个值来对应，字典的键和值
    print("\nKey: " + key)
    print("Value: " + value)

print("-" * 26, '\n')

# 只遍历字典中的 key
for atrr in user_0.keys():
    print(atrr)

print(list(user_0.keys()))  # 我们可以通过这种方式变成列表

print("-" * 26, '\n')

# 只遍历字典中的 value
for val in user_0.values():
    print(val)
print(list(user_0.values()))  # 同理与上面那个

# 利用 set 筛选出不重复的组成一个集
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', }
for language in set(favorite_languages.values()):  # 使用 set 命令处理字典.value() 返回的列表，挑除重复的元素
    print(language.title())

# 让我们来看看 set 后的本质
a = set(favorite_languages.values())    # 虽然和字典一样都是 {} 但是集就是单纯的一个键，没有对应的值，操作和 list 类似
