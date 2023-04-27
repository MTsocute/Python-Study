from collections import OrderedDict

favorite_languages = OrderedDict()  # 有序的空字典类，其实就是字典，但是创建的时候，没有用 {}

favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c' 
favorite_languages['edward'] = 'ruby' 
favorite_languages['phil'] = 'python'


for name, language in favorite_languages.items(): 
    print(name.title() + "'s favorite language is " + language.title() + ".")


import random

x = random.randint(1,6)
print(f'在 1～6随机生成：{x}')