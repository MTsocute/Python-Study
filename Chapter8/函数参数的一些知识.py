# 1、函数，（形参1，形参2）
def pet_fun(pet_name, owner_name):
    print(f'{pet_name}\'s owner is {owner_name}')


# 2、当然我们甚至还可以给形参赋默认值，如果不修改就是一直用这个
def say_hello(someone_say_hello_to='Momo'):
    print(f'Hello, {someone_say_hello_to}')


# 3、默认参数使得参数变成可选择性的
def get_formatted_name(first_name, last_name, middle_name=''):  # 我们把参数默认为''，实现了参数可选择化
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()  # 返回名字


if __name__ == '__main__':
    # 1、函数可以多个参数按照顺序默认赋值
    pet_fun("Wang", "Momo")

    # 1、但是，如果顺序不对就会闹出笑话来了，譬如
    pet_fun("Momo", "Wang")  # 主人和宠物的顺序位置颠倒了

    # 1、为了避免上述情况的发生，就有了对关键字赋值的功能
    pet_fun(owner_name="Momo", pet_name="Wang")  # 如此一来，我们就不用考虑顺序问题了

    # 2、如果不修改默认值，就相当于默认是 someone_say_hello_to='Momo'
    say_hello()
    # 2、对比下赋参
    say_hello("BugYello")

    # 3、选择性参数
    musician = get_formatted_name('jimi', 'hendrix')  # 没有中间名的时候
    print(musician)
    musician = get_formatted_name('john', 'hooker', 'lee')
    print(musician)
