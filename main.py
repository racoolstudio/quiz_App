# pass keyword
# class User:
#     def __init__(self,  car):
#         self.car = car
#     pass
import quiz_brain
import question_model
import data

question_bank = []
for i in data.question_data:
    question_text = i['text']
    question_answer = i['answer']
    question_bank.append(question_model.QuestionModel(question_text, question_answer))
quiz1 = quiz_brain.QuizBrain(question_bank)
isStart = True
while isStart:
    quiz1.display()
    quiz1.check()
    isStart = quiz1.next_question()


