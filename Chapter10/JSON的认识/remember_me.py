# 在这里呢，我们主语要来体会下，分门别类的处理某一个功能，这样子的理念
import json

# 这个函数一个完成了很多功能，过于冗杂，我们可以将其拆分成多个来完成其功能
def greet_user():
    """
        和用户打招呼，如果有json 文件就会直接和里面的用户打招呼。
        如果没有就会创建一个，让用户输入名字，再一次调用的时候，就会打招呼了！
    """
    filename = '/Users/momo/Desktop/Python/Chapter10/JSON的认识/username.json' 
    try:
        with open(filename) as f_obj: username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ") 
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!") 
    else:
        print("Welcome back, " + username + "!")


# 重构
def get_stored_username(FileName):
    """
        FileName：文件所在的绝对路径（包括文件本身）
        Return：
            1、若函数存在就会返回里面的数据
            2、不存在就会返回 False
    """
    try:
        with open(filename) as f_obj: 
            try:
                username = json.load(f_obj)
            # 防止文件内容为空
            except json.JSONDecodeError:
                print("There is no data in json, plz input your name!")
                username = None
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_name(FileName):
    with open(FileName, 'w') as f_obj:
        username = input("What is your name: ")
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!") 


def greet_user_2(FileName):
    """
        和用户打招呼
        如果有json 文件就会直接和里面的用户打招呼。
        如果没有就会创建一个，让用户输入名字，再一次调用的时候，就会打招呼了！
    """
    username = get_stored_username(FileName)
    if username:
        print(f'Is {username} your name?')
        judge = input("plz input yes or no: ")
        if judge.lower() == 'yes':
            print("Welcome back, " + username + "!")
        else:
            get_new_name(FileName)
    else:
        username = get_new_name(FileName)


filename = '/Users/momo/Desktop/Python/Chapter10/JSON的认识/username.json' 
greet_user_2(filename)