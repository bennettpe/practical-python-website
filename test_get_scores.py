import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

def scores_list():
    """
    Get player-scores.txt and convert to tuples.  Sort the score in each tuple 
    to return the top 3 scores to the leader board.
    """
    li = [i.replace(":" , "").replace("'" , "").split() for i in open('./data/capitals/capitals_leaders.txt').readlines()]
    print(li)
    li.sort(key=lambda tup: tup[1]) # picks out the score from (Score:, 10, Player:, MyName, Date:, 16/08/2018)
    li.sort(reverse=True)           # sorts scores from highest to lowest

    # Cleanup the tuple data by striping and replacing unwanted characters, for rendering to html
    first  = str(li[0])[1:-1].replace("'" , " ").replace("," , " ")
    second = str(li[1])[1:-1].replace("'" , " ").replace("," , " ")
    third  = str(li[2])[1:-1].replace("'" , " ").replace("," , " ")
    fourth = str(li[3])[1:-1].replace("'" , " ").replace("," , " ")
    return first, second, third, fourth 
    print(first)
    print(second)
    print(third)
    print(fourth)
    
    scores = scores_list()
    print(scores)