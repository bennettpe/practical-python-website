import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

# ----------------------------#
# Split answer file function #
# ----------------------------#  
def split_answer_file(filename):
    answers = {}
    with open(filename,"r") as file:
        for line in file.readlines():
           splitdata = line.split(":") # this gives you a list of what's on either side of ':'
           answers[splitdata[0]] = splitdata[1].strip() # give the answers dict a key of the first list item and a value of the 2nd
    return answers
    
correct_answers = split_answer_file('./data/geography1/geography1_correct_answer.txt') 
print('Dict Correct\t',correct_answers)

incorrect_answers = split_answer_file('./data/geography1/geography1_incorrect_answer.txt') 
print('Dict Incorrect\t',incorrect_answers)