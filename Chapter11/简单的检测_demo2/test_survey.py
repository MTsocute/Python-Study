import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """ 针对AnonymousSurvey的测试 """
    
    def test_store_single_response(self): 
        """测试单个输入是否会被正常存储"""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English')
        
        # self.assertEqual(my_survey.responses[0], 'English') # 老的方法
        self.assertIn('English', my_survey.responses) # 新的方法
    
    def test_store_three_response(self): 
        """测试三个输入是否会被正常存储"""
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 

        responses = ['English', 'German', 'Chinese']

        for answer in responses:
            my_survey.store_response(answer)
        
        for language in responses:
            self.assertIn(language, my_survey.responses) # 新的方法

unittest.main()