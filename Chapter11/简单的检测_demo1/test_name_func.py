import unittest
from name_func import get_formatted_name


# 名字中最好带有 Test
class NamesTestCase(unittest.TestCase):  # 这个必须要继承单元测试类
    """ 这个类下的所有方法都是为了测试函数能否正常运行 """

    # 测试一个函数
    def test_first_last_name(self):
        """ 能够顺利的处理名字嘛 """
        formatted_name = get_formatted_name('janis', 'joplin')  # 被测试的函数
        """ unittest.assertEqual()，
        断言测试，检测是否值和我们预期的一致 """
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """ 能够顺利处理有中间名的函数嘛 """
        formatted_name = get_formatted_name('janis', 'joplin', 'J.K')
        self.assertEqual(formatted_name, 'Janis J.K Joplin')


unittest.main()
