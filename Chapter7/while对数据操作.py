unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 利用 while 实现，从非确定用户中一一选出，然后放到确定用户的操作
while unconfirmed_users:  # 只要列表不为空就是 True
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示确认列表中的所有成员
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 利用 while 实现删除利用表中所有指定元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:    # 这个多次删除实现相对 for 来说方便的多了
    pets.remove('cat')
print(pets)
