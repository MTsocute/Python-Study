import unittest
from city_func import city_and_country

class CityTestCase(unittest.TestCase):
    """ 测试 city_func.py 下函数是否正常"""

    def test_city_func(self):
        """ 检测 city_func 是否成功运行 """
        formatted_city_country = city_and_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago,Chile')

    def test_city_func_population(self):
        """ 检测 city_func 带人口参数是否能够运行成功 """
        formatted_city_country = city_and_country('Santiago', 'Chile', '50000000')
        self.assertEqual(formatted_city_country, 'Santiago,Chile - 50000000')

unittest.main()