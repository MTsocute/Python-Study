# 写入多行：注意，w 会覆盖原本所有的内容！
with open("/Users/momo/Desktop/Python/Chapter10/data/pro.txt", "w") as file_obj:
    file_obj.write("I love Python\n")
    file_obj.write("I enjoy Python\n")
    print("End~~")

# 附加
with open("/Users/momo/Desktop/Python/Chapter10/data/pro.txt", "a") as file_obj:
    file_obj.write("I love C\n")
    file_obj.write("I enjoy C\n")
    print("End~~")