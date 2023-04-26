# 使用 * 接收多个参数
def order_food(*topping):
    """
        *参数: 创建一一个为toppings的空元组组，并将接收到到的所有内容都存在里面
    """
    print(topping)


# 我们接收多个不同类型的参数看看，会怎么样
order_food(
    'pizza',
    ['Cola', 'Tea', 'Fresh_Lemon'],
    {
        'Child_Set': ['Banana', 'Beef'],
        'KFC_Set': 'Hamburger'
    }
)

# 结果
"""
    使用元组包装起来了
    (
        'pizza', 
        ['Cola', 'Tea', 'Fresh_Lemon'], 
        {'Child_Set': ['Banana', 'Beef'], 'KFC_Set': 'Hamburger'}
    )
"""

# 使用 ** 接收多个 关键字 + 参数
def User_Info(**u_info):
    """
        **参数：创建值一个字典，存储消息
    """
    print(u_info)


User_Info(Name="Helen", Location="Germany", IQ="High")


# 结果
"""
    {'Name': 'Helen', 'Location': 'Germany', 'IQ': 'High'}
"""


# 但是我们在这里也要提出一个问题，我们既然可以传递那么多不同的类型，我们应该如何保证一一接收呢?或者按照我们的意愿来接收呢？

# Demo_1: 我们需要的放前面，多余的放后面的，一对一操作法
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Demo_2：需要接收任意数量的实参，但预先不知道传递给函数的会是什么样的信息
