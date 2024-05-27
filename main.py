# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:19:07 2023

@author: Mansoor
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
q_bank = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_question = Question(q_text, q_answer)
    q_bank.append(new_question)

quiz = QuizBrain(q_bank)
while quiz.still_have_question():
    quiz.next_question()