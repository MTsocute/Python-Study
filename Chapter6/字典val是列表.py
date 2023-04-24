pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],  # 注意这个 key 对应的 val 是一个 list
}

# 让我们来遍历下这个pizza的所有配料吧
for top in pizza['toppings']:
    print(top)

# 来一个复杂一点点的情况
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'], 'phil': ['python', 'haskell'],
}

# val 列表字典的遍历
print(favorite_languages.items())  # .items() 会把字典变成 [(), (), ()] 列表中有元组的结构，可以用于赋值
for k, v in favorite_languages.items():
    print(k, v)  # 这个时候，k对应的键，v对应的列表
