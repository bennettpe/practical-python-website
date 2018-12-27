import os 
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for
from natsort import natsorted

def sortkey(n):
    return n[3]
    
def get_leaders_file(filename):
    score_players = []
    with open(filename,"r") as file:
         for line in file.readlines():
             score_players.append(line)
           
         sorted_players = []
         for player in score_players:
             tup = (player.split(':')[0],
                    player.split(':')[1], 
                    player.split(':')[2], 
                    player.split(':')[3].strip())
             sorted_players.append(tup)
         return natsorted(sorted_players,key=sortkey,reverse=True)[:6] # natural sort , highest first, top 6 
         
sorted_top = get_leaders_file('./data/geography1/geography1_leaders.txt') 
print('Scores\t',sorted_top)  
sorted_top = get_leaders_file('./data/capitals/capitals_leaders.txt') 
print('Scores\t',sorted_top)