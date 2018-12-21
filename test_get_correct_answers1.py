import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

def get_answers(filename):
    question = []
    with open(filename, "r") as question:
        question = [row for row in question]
        return question[-18:]
        
correct_answers = get_answers('./data/geography1/geography1_correct_answer.txt') 

split_list =[i.split(':') for i in correct_answers]
print(split_list)



#question_number =[]
#question_answer =[]
#question_number = correct_answers.split(':')[0]
#question_answer = correct_answers.split(':')[1]

#print(question_number)
#print(question_answer)