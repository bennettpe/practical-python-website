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
         for line in file: 
           question.append(line)  
           print(question)
