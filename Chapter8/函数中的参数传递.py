# 我们传递的参数，不一定只能是简单的单一数据，甚至可以是列表
def greet_users(names):
    """
    给列表中的每一个成员打招呼
    :param names: 一个列表，里面是要求是字符串
    """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


