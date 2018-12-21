import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

# Getting the answer function - START
# -----------------------------------------#
# Read correct or incorrect txt files     #
# and split into question number , answer #
# -----------------------------------------#
def get_answers(filename):       
    with open(filename,"r") as file:
         question = []
         for line in file.readlines(): 
           question.append(line)  
         
         split_answer = []
         for answer in question:
             question_number = answer.split(':')[0]
             question_answer = answer.split(':')[1]
             print(question_number)
             print(question_answer)
             #split_question = (answer.split(':')[0].strip(), (answer.split(':')[1].strip()))
             #split_answer.append(split_question)
         return question_number[-18:]    
#Getting the answer function - END

correct_answers = get_answers('./data/geography1/geography1_correct_answer.txt') 
print(correct_answers)

#question_number =[]
#question_number = correct_answers.split(':')[0]
#question_answer = correct_answers.split(':')[1]
#print(question_number)        
#print(question_answer)