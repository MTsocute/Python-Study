# 一次读完
def read_all(flie_path, flie_name):
    with open(flie_path + flie_name) as file_object: 
        contents = file_object.read() 
        print(contents)

# 逐行读取，但是字符串
def line_by_line(flie_path, flie_name):
    with open(flie_path + flie_name) as file_obj:
        for line in file_obj:
            print(line.rstrip('\n'))    # 去除自动换行符(每一行末尾自带)

# 逐行读取，但是列表
def line_by_line_2(flie_path, flie_name):
    with open(flie_path + flie_name) as file_obj:
        lines = file_obj.readlines()

    # 去除自动换行符
    for line in lines:
        print(line.rstrip('\n'))

    return lines


if __name__ == '__main__':
    file_path = '/Users/momo/Desktop/Python/Chapter10/data/'
    file_name = 'pi.txt'

    # read_all(file_path, file_name)
    # line_by_line(file_path, file_name)
    # line_by_line_2(file_path, file_name)