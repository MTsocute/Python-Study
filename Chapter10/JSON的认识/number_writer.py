import json

numbers = [2, 3, 5, 7, 11, 13]
filename = '/Users/momo/Desktop/Python/Chapter10/data/numbers.json'

# 写一个 json 文件，存储内容为一个列表
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)  # 你会发现 json 里面写的不是字符串，而是一个列表机构
    print("End~")
