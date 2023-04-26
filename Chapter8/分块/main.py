"""
    我们可以在其他模块完成对函数的制作，然后再导入主要函数部分实现代码，
    这样子的话，我们每一个模块实现一个功能，最后在拼接就好啦
"""

import pizza as pz  # 我们把 pizza.py 作为模块导入了，然后令其名为 pz

# 调用 pizza.py 里面的函数
pz.make_pizza(16, 'pepperoni')
pz.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

print()

# 当然，我们可以也只导入其中一个函数
from pizza import say_hello as sh
sh()

print()

# 我们可以导入 pizza.py 的所有内容，这个时候使用里面的函数就不再需要 模块名.函数(),直接函数就行
from pizza import *     # 这个注意，还是不建议那么做，如果别人写的全局变量名和你的一样可能有冲突了
curse()