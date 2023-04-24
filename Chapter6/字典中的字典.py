users = {
    # 第一个用户
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    # 第二个用户
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# 查看字典中的所有用户
# for user in users:
#    print(user)


# 把字典中的用户变成 列表元组 模式
for user_name, user_data in users.items():
    # print(users.items())    # 注意元组中的参数，('字符串', {字典})
    print("User:", user_name.title())
    print("\tFull Name: " + user_data['first'].title() + " " + user_data['last'].title())
    print("\tLocation: " + user_data['location'].title())
