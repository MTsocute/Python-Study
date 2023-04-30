def count_word(filePath, filename):
    count = 0   # 记录单词出现的总数
    try:
        with open(filePath + filename) as f_obj:
            contents = f_obj.readlines()    # 读取所有内容返回，每一行作为列表一个内容
            # print(contents)
    
    except FileNotFoundError:       # 文件找不到的处理
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    
    else:   # 如果没有找不到这种问题，就继续走
        str = input("请输入你想查找数量的单词:")
        for line in contents:   # 读取每一行
            line = line.strip() # 去除每一行的前后空格和换行符
            count += (line.lower()).count(str)  # 找到字符串中对应内容的个数，并记录
        print(f'The file \" {filename} \" has about {count} of {str}.')


if __name__ == '__main__':
    filepath = "/Users/momo/Desktop/Python/Chapter10/data/"
    count_word(filepath, filename="inpython.txt")