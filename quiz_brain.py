

class QuizBrain:

    def __init__(self, question_list, number=0):
        self.number = number
        self.question_list = question_list
        self.answer = ''
        self.score = 0

    def display(self):

        self.answer = input(f'Q.{self.number+1}: {self.question_list[self.number].display_question()} (True/False) :').lower()

    def check(self):

        if self.answer == self.question_list[self.number].display_answer().lower():
            self.score += 1
            print(f'You are right ! ✅' )
        else:
            print(f'You are wrong ! ❌ ')
        self.number += 1
        print(f'Current Score:{self.score}/{self.number}')

    def next_question(self):
        if self.number < len(self.question_list) :
            return QuizBrain(self.question_list[self.number], self.number+1)
        print('You are Done!!! 👑🫡💵')
        return False


