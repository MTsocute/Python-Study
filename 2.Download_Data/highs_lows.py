import csv
import matplotlib.pyplot as plt

filename = '/Users/momo/Desktop/Python/' \
           'data_visiable/2.Download_Data/datas/sitka_weather_07-2014.csv'

# 从文件中提取，最高温
with open(filename) as f:
    # csv 文件打开方式
    reader = csv.reader(f)
    # 调用函数一次，就返回一行，所以我们看到的是开头
    header_row = next(reader)  # 把标题行单独赋出来
    highs = []
    # 标题行已经分配走了，遍历的就是后面的数据了
    for row in reader:
        # print(row)
        # 表第二列数据就是当天的最高温
        high = int(row[1])      # 转换成 int 以便于 matplotlib 读取
        highs.append(high)

# 查看标题行
# for index, column_num in enumerate(header_row):
#     print(f'{index}\t{column_num}')

print(highs)
