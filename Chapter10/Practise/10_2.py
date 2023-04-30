import sys
"""
    # sys 会把当前文件定位在 Chapter10 下，否则下面的 import 会找不到相对位置
    # 处理这个问题的最好的方法，还是在 Chapter10 创建 __init__.py 
    # 如此一来的话，这个文件夹里面的任何文件都可以当作为模块导入了
"""
sys.path.append("/Users/momo/Desktop/Python/Chapter10/") 
import file_reader  


if __name__ == '__main__':
    File_path = '/Users/momo/Desktop/Python/Chapter10/data/'
    File_name = 'inpython.txt'
    
    ls = file_reader.line_by_line_2(flie_name=File_name, flie_path=File_path)
    print()
    for line in ls:
        print(line.replace('python', 'c').rstrip())