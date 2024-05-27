# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:19:29 2023

@author: Mansoor
"""

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
        
    def next_question(self):
        self.current_question = self.q_list[self.question_number].q_text
        self.question_number+=1
        user_answer = input(f'Q.{self.question_number}: {self.current_question} (True/False) : ')
        self.validate_answer(user_answer)
        
    def still_have_question(self):
        if self.question_number >= len(self.q_list):
            return False
        return True
    
    def validate_answer(self, answer):
        self.current_answer = self.q_list[self.question_number-1].q_answer
        if(answer.lower()==self.current_answer).lower():
            self.score+=1
            print('You got it right')
            print(f'The correct answer is {self.current_answer}')
            print(f'Your score is {self.score}/{self.question_number}')
      
        else:
            print("That's Wrong")
            print(f'The correct answer is {self.current_answer}')
            print(f'Your score is {self.score}/{self.question_number}')