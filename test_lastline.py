import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

# ------------------------------------------------------#
# Get last username,number of questions,score function #
# ------------------------------------------------------#
def get_last_line(filename):  
    with open(filename, 'r') as file:
        last_line = file.readlines()[-1]  
        return last_line
        
last_line = get_last_line('./data/geography1/geography1_leaders.txt')   

final_count    = []
final_date     = []
final_score    = []
final_username = []

final_date     = last_line.split(':')[0]
final_username = last_line.split(':')[1]
final_count    = last_line.split(':')[2]
final_score    = last_line.split(':')[3]

print(last_line)        
print(final_date)
print(final_username)
print(final_count)
print(final_score)
        