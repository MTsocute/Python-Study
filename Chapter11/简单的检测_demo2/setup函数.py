import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    
    # 经由 setUp() 创建的对象，可以供测试函数直接使用
    def setUp(self):
        """
            创建一个调查对象和一组答案，供使用的测试方法测试
            即：我们不需要对每一个函数都生成一个类然后调用方法
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)              # 创建一个调查对象
        self.responses = ['English', 'Spanish', 'Mandarin']     # 创建一个回答列表


    def test_single_store(self):
        """
            测试一个存储，是够能正常运行
        """
        # 直接调用 setUp() 创建的 AnonymousSurvey() 对象
        self.my_survey.store_response(self.responses[0])  # 存储一个回答
        # 检验：‘English’ 是否存储到，调查对象的回答列表中去了
        self.assertIn(self.responses[0], self.my_survey.responses)


    def test_store_three_response(self): 
        """
            测试三个输入是否会被正常存储
        """
        for answer in self.responses:
            self.my_survey.store_response(answer)
        
        for language in self.responses:
            self.assertIn(language, self.my_survey.responses)

unittest.main()