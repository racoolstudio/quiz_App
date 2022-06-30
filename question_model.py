import data


class QuestionModel:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


    def display_question(self):
        return self.question

    def display_answer(self):
        return self.answer



