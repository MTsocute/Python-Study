favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

# 我们接来下，就不需要两个变量页可以遍历所有的键和值
for name in favorite_languages.keys():
    print(name.title() + "\'s favorite language is " + favorite_languages[name].title())
