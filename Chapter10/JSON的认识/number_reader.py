import json

filename = '/Users/momo/Desktop/Python/Chapter10/data/numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)  # 把列表格式的数据读入本文件
    numbers.append(114514)  # 真的可以当作数组来用
    print(numbers)