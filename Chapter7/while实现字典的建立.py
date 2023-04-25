polling_active = True
responses = {}   # 用于收集信息的字典

while polling_active:
    # 收集信息
    name = input("What is your name? \n")
    answer = input("Which mountain would you like to climb someday?\n")

    # 把收集到的信息收集在字典当中去
    responses[name] = answer

    # 看是否还有人要回答问卷
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# 显示调查问卷的结果
print("-- Result --")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")