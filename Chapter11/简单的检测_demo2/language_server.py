from survey import AnonymousSurvey

question = "What language did you first learn to speak?" 

my_survey = AnonymousSurvey(question)
my_survey.show_question()

# 创建循环，把自己的回答存入答案里列表中
print("Enter 'q' at any time to quit.\n") 
while True:
    response = input("Language: ") 
    if response == 'q':
        break 
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!") 
my_survey.show_results()    # 暂时答案