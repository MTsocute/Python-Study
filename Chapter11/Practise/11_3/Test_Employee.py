import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.my_emp_1 = Employee('mo', 'mo', 1000)
        self.my_emp_2 = Employee('mo', 'mo', 1000)

    def test_give_default_raise(self):
        """
            测试：不给值，是否默认加薪 5000
        """
        self.my_emp_1.give_money()
        self.assertEqual(6000, self.my_emp_1.salary)
    
    def test_give_custom_raise(self):
        """
            测试：给定加薪值，看是否加薪
        """
        self.my_emp_2.give_money(3000)
        self.assertEqual(4000, self.my_emp_2.salary)
        

unittest.main()