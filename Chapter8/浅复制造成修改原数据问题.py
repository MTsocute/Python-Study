# 这个相当于是浅复制，会导致ls1，就是原数据本身，对其修改就是会影响原列表
def mod_arr_1(ls1):
    ls1.append(4)
    return ls1


list_a = [1, 2, 3]

li_1 = mod_arr_1(list_a)

print(f'浅复制：{li_1}')
print(f'原数据：{list_a}')

print("~" * 32)


# 为了解决浅复制对原数据造成影响，我们可以使用深复制来解决该问题
def mod_arr_2(ls_1):
    ls_2 = ls_1.copy()  # 注意这里，ls_2 就独立于 ls_1 了，是一个新列表
    ls_2.append(4)
    return ls_2


list_b = [1, 2, 3]
li_2 = mod_arr_2(list_b)

print(f'深复制：{li_2}')
print(f'原数据：{list_b}')
