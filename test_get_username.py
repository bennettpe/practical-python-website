import os 
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for
from natsort import natsorted

# ------------------------------------#
# Get Username for capitals category #
# ------------------------------------#
def capitals_get_username():
    player = 'Paul'   
    player = player.lower()
    with open('./data/capitals/capitals_username.txt', 'r') as username_list:
        active_username = username_list.read().splitlines()
        if player in active_username:
            message = "username taken"
        else: 
            message = "username not taken"
            file = open('./data/capitals/capitals_username.txt', 'a')
            file.write(player + '\n')  
    print(message)
 
capitals_get_username()       