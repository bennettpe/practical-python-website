import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for
from natsort import natsorted

    
# -------------------------------- #
# Count question_numbers function #
# ---------------------------------#
def count_my_question_numbers(filename):
    with open(filename, 'r') as json_data:
        data = json.load(json_data)
    return len(data)
    
    
# --------------------- #
# Create date function #
# ----------------------#
def create_date():
    date_format = '%d/%m/%y'
    get_date = datetime.now().strftime(date_format)
    return get_date


# -------------------------------------------------#
# Get username,number of questions,score function #
# -------------------------------------------------#
def get_leaders_file(filename):
    score_players = [] 
    with open(filename,"r") as file:
         for line in file.readlines():
             score_players.append(line)
           
         sorted_players = []
         for player in score_players:
             tupe = (player.split(':')[0], 
                     player.split(':')[1], 
                     player.split(':')[2], 
                     player.split(':')[3].strip())
             sorted_players.append(tupe)
         return natsorted(sorted_players,key=sortkey,reverse=True)[:6] # natural sort , highest first, top 6 
 
         
# -------------------------#
# Reading a file function #
# -------------------------#    
def read_from_file(filename):
	with open(filename,"r") as file:
		data = file.readlines()
		return data

		
# ------------------#
# Sortkey function #
# ------------------#  
def sortkey(n):
    return n[3]

   
# ---------------------------------------#
# Split answer file function            #
# Create dict and split into key, value #
# ---------------------------------------#  
def split_answer_file(filename):
    answers = {} # create dict
    with open(filename,"r") as file:
        for line in file.readlines():
           splitdata = line.split(":") 
           answers[splitdata[0]] = splitdata[1].strip() 
    return answers
    
    
# --------------------------#
# Writing to file function #
# --------------------------#
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)    

        
# ------------------------------------------------------#
# Get last username,number of questions,score function #
# ------------------------------------------------------#
def get_last_line(filename):  
    with open(filename, 'r') as file:
         last_line = file.readlines()[-1]  
         last_count    = []
         last_date     = []
         last_score    = []
         last_username = []
         last_date     = last_line.split(':')[0]
         last_username = last_line.split(':')[1]
         last_count    = last_line.split(':')[2]
         last_score    = last_line.split(':')[3]
         return last_count, last_date, last_score, last_username
 
        
app = Flask(__name__)
# Key generated from Secretkey.py
app.secret_key = "b'\xa0\xba+\xe5\xaa\x8b\xac\x01\x96\x1f<)86\x84\x04" 


# --------------------------------#
# Route Decorator for index.html #
# --------------------------------#
@app.route('/')
def index():
    return render_template('index.html')

 
# ------------------------------------#
# Get Username for capitals category #
# ------------------------------------#
@app.route('/capitals_get_username', methods=['GET', 'POST'])
def capitals_get_username():

    catname  = 'Odd One Out Capitals'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    message  = []
    player   = []
    urlname  = '/capitals_get_username'
    urlforname = '/capitals_sign_in'
    
    if request.method == 'POST':
        with open('./data/capitals/capitals_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                message = "username taken"
                print(urlforname) 
            else: 
                file = open('./data/capitals/capitals_username.txt', 'a')
                file.write(player + '\n')  
                open('./data/capitals/capitals_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/capitals/capitals_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('capitals_user'))  
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)   


# --------------------------------#
# Sign in  for capitals category #
# --------------------------------#
@app.route('/capitals_sign_in', methods=['GET', 'POST'])
def capitals_sign_in():
    
    catname  = 'Odd One Out Capitals'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    message  = []
    player   = []
    urlname  = '/capitals_sign_in'
    urlforname = '/capitals_get_username'
   
    if request.method == 'POST':
        with open('./data/capitals/capitals_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/capitals/capitals_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/capitals/capitals_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('capitals_user', capitals_username = request.form['get_username']))   
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player)   

    
# -----------------------------------#
# Read   capitals jsonfile          #
# Render capitals_quiz.html page    #
# -----------------------------------#
@app.route('/capitals_user<capitals_username>', methods=['GET', 'POST'])
def capitals_user(capitals_username):

    catname       = 'Odd One Out Capitals'
    catnum        = 'Four'
    cattext       = 'Can you choose the capital that is NOT on the given continent'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    questions     = []
    
    with open('./data/capitals/odd_one_out_capitals.questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/capitals/odd_one_out_capitals.questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer   = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/capitals/capitals_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/capitals/capitals_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False
                
            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/capitals/capitals_leaders.txt'
                               , str(todays_date) + ':'
                               + capitals_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect('capitals_completed_quiz')

    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = capitals_username
                           )    
 
  
# -------------------------------------------#
# Read   capitals_leaders.txt file         #
#        capitals_correct_answer.txt       #
#        capitals_incorrect_answer.txt     #
# Render capitals_quiz_completed.html page #
# -------------------------------------------#
@app.route('/capitals_completed_quiz', methods=['GET', 'POST'])
def capitals_completed_quiz():  
    
    catname  = 'Odd One Out Capitals'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    
    last_count, last_date, last_score, last_username = get_last_line('./data/capitals/capitals_leaders.txt') 
    correct_answers   = split_answer_file('./data/capitals/capitals_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/capitals/capitals_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )
                          
                                                     
# --------------------------------------#
# Get Username for geography1 category #
# --------------------------------------#
@app.route('/geography1_get_username', methods=['GET', 'POST'])
def geography1_get_username():

    catname  = 'Geography 1'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    message  = []
    player   = []
    urlname  = '/geography1_get_username'
    urlforname = '/geography1_sign_in'
    
    if request.method == 'POST':
        with open('./data/geography1/geography1_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                message = "username taken"
            else: 
                file = open('./data/geography1/geography1_username.txt', 'a')
                file.write(player + '\n')  
                open('./data/geography1/geography1_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/geography1/geography1_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('geography1_sign_in', geography1_username = request.form['get_username']))
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)


# ---------------------------------#
# Sign in for geography1 category #
# ---------------------------------#
@app.route('/geography1_sign_in', methods=['GET', 'POST'])
def geography1_sign_in():
    
    catname  = 'Geography 1'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    message  = []
    player   = []
    urlname  = '/geography1_sign_in'
    urlforname = '/geography1_get_username'
    
    if request.method == 'POST':
        with open('./data/geography1/geography1_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/geography1/geography1_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/geography1/geography1_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('geography1_user', geography1_username = request.form['get_username']))
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlfornme=urlforname, signin_message=message, username_player=player) 
    
    
# -------------------------------------#
# Read   geography1 jsonfile          #
# Render geography1_quiz.html page    #
# -------------------------------------#
@app.route('/geography1_user<geography1_username>', methods=['GET', 'POST'])
def geography1_user(geography1_username):

    catname       = 'Geography1'
    cattext       = 'How many questions do you know in Geography1'
    catnum        = 'Four'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    questions     = []
    
    with open('./data/geography1/geography1_questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/geography1/geography1_questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer   = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/geography1/geography1_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/geography1/geography1_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False
                
            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/geography1/geography1_leaders.txt'
                               , str(todays_date) + ':'
                               + geography1_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect(url_for('geography1_completed_quiz', category = catname, img_id = imgname))
                
    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = geography1_username
                          )
                          
                           
# --------------------------------------------#
# Read   geography1_leaders.txt file         #
#        geography1_correct_answer.txt       #
#        geography1_incorrect_answer.txt     #
# Render geography1_quiz_completed.html page #
# --------------------------------------------#
@app.route('/geography1_completed_quiz', methods=['GET', 'POST'])
def geography1_completed_quiz():  
    
    catname  = 'Geography1'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
  
    last_count, last_date, last_score, last_username = get_last_line('./data/geography1/geography1_leaders.txt') 
    correct_answers   = split_answer_file('./data/geography1/geography1_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/geography1/geography1_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )
                          
                          
# --------------------------------------#
# Get Username for geography2 category #
# --------------------------------------#
@app.route('/geography2_get_username', methods=['GET', 'POST'])
def geography2_get_username():

    catname  = 'Geography 2'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    message  = []
    player   = []
    urlname  = '/geography2_get_username'
    urlforname = '/geography2_sign_in'
    
    if request.method == 'POST':
        with open('./data/geography2/geography2_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
               message = "username taken"
            else: 
                file = open('./data/geography2/geography2_username.txt', 'a')
                file.write(player + '\n')  
                open('./data/geography2/geography2_completed_quiz_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/geography2/geograpjy2_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('geography2_sign_in', geography2_username = request.form['get_username']))
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player) 


# ---------------------------------#
# Sign in for geography2 category #
# ---------------------------------#
@app.route('/geography2_sign_in', methods=['GET', 'POST'])
def geography2_sign_in():
    
    catname  = 'Geography 2'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    message  = []
    player   = []
    urlname  = '/geography2_sign_in'
    urlforname = '/geography2_get_username'
    
    if request.method == 'POST':
        with open('./data/geography2/geography2_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/geography2/geography2_completed_quiz_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/geography2/geograpjy2_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('geography2_user', geography2_username = request.form['get_username']))   
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player) 


# -------------------------------------#
# Read   geography2 jsonfile          #
# Render geography2_quiz.html page    #
# -------------------------------------#
@app.route('/geography2_user<geography2_username>', methods=['GET', 'POST'])
def geography2_user(geography2_username):

    catname       = 'Geography2'
    cattext       = 'How many questions do you know in Geography2'
    catnum        = 'Four'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    questions     = []
    
    with open('./data/geography2/geography2_questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/geography2/geography2_questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer  = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/geography2/geography2_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/geography2/geography2_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False

            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/geography2/geography2_leaders.txt'
                               , str(todays_date) + ':'
                               + geography2_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect('geography2_completed_quiz')

    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = geography2_username
                           )


# --------------------------------------------#
# Read   geography2_leaders.txt file         #
#        geography2_correct_answer.txt       #
#        geography2_incorrect_answer.txt     #
# Render geography2_quiz_completed.html page #
# --------------------------------------------#
@app.route('/geography2_completed_quiz', methods=['GET', 'POST'])
def geography2_completed_quiz():  
    
    catname  = 'Geography2'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    
    last_count, last_date, last_score, last_username = get_last_line('./data/geography2/geography2_leaders.txt') 
    correct_answers   = split_answer_file('./data/geography2/geography2_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/geography2/geography2_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )
                          
                          
# -----------------------------------#
# Get Username for highest category #
# -----------------------------------#
@app.route('/highest_get_username', methods=['GET', 'POST'])
def highest_get_username():

    catname  = 'Highest'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    message  = []
    player   = []
    urlname  = '/highest_get_username'
    urlforname = '/highest_sign_in'

    if request.method == 'POST':
        with open('./data/highest/highest_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                message = "username taken"
            else: 
                file = open('./data/highest/highest_username.txt', 'a')
                file.write(player + '\n')  
                open('./data/highest/highest_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/highest/highest_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('highest_sign_in', highest_username = request.form['get_username']))
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)    


# ---------------------------------#
# Sign in for highest category #
# ---------------------------------#
@app.route('/highest_sign_in', methods=['GET', 'POST'])
def highest_sign_in():
    
    catname  = 'Highest'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    message  = []
    player   = []
    urlname  = '/highest_sign_in'
    urlforname = '/highest_get_username'
    
    if request.method == 'POST':
        with open('./data/highest/highest_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/highest/highest_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/highest/highest_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('highest_user', highest_username = request.form['get_username']))   
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player) 


# ----------------------------------#
# Read   highest jsonfile          #
# Render highest_quiz.html page    #
# ----------------------------------#
@app.route('/highest_user<highest_username>', methods=['GET', 'POST'])
def highest_user(highest_username):

    catname       = 'Highest'
    cattext       = 'Can you choose which city has the HIGHEST elevation above sea level'
    catnum        = 'Three'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    questions     = []
    
    with open('./data/highest/which_city_has_the_highest_elevation_above_sea_level.questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/highest/which_city_has_the_highest_elevation_above_sea_level.questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer  = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/highest/highest_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/highest/highest_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False

            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/highest/highest_leaders.txt'
                               , str(todays_date) + ':'
                               + highest_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect('highest_completed_quiz')

    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = highest_username
                           )
                           
                           
# -----------------------------------------#
# Read   highest_leaders.txt file         #
#        highest_correct_answer.txt       #
#        highest_incorrect_answer.txt     #
# Render highest_quiz_completed.html page #
# -----------------------------------------#
@app.route('/highest_completed_quiz', methods=['GET', 'POST'])
def highest_completed_quiz():  
    
    catname  = 'Highest'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    
    last_count, last_date, last_score, last_username = get_last_line('./data/highest/highest_leaders.txt') 
    correct_answers   = split_answer_file('./data/highest/highest_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/highest/highest_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )
                          
                                                           
# -----------------------------------#
# Get Username for islands category #
# -----------------------------------#
@app.route('/islands_get_username', methods=['GET', 'POST'])
def islands_get_username():

    catname  = 'Islands'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    message  = []
    player   = [] 
    urlname  = '/islands_get_username'
    urlforname = '/islands_sign_in'

    if request.method == 'POST':
        with open('./data/islands/islands_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                message = "username taken"
            else: 
                file = open('./data/islands/islands_username.txt', 'a')
                file.write(player + '\n')  
                open('./data/islands/islands_correct_answer.txt', 'w').close()  
                open('./data/islands/islands_incorrect_answer.txt', 'w').close()
                return redirect(url_for('islands_user'))
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)    


# -------------------------------#
# Sign in for islands category #
# -------------------------------#
@app.route('/islands_sign_in', methods=['GET', 'POST'])
def islands_sign_in():
    
    catname  = 'Islands'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    message  = []
    player   = []
    urlname  = '/islands_sign_in'
    urlforname = '/islands_get_username'
    
    if request.method == 'POST':
        with open('./data/islands/islands_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/islands/islands_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/islands/islands_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('islands_user', islands_username = request.form['get_username']))   
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player) 
    
    
# ----------------------------------#
# Read   islands jsonfile          #
# Render islands_quiz.html page    #
# ----------------------------------#
@app.route('/islands_user<islands_username>', methods=['GET', 'POST'])
def islands_user(islands_username):

    catname       = 'Islands'
    cattext       = 'Can you choose which COUNTRY lays claim to each of these islands'
    catnum        = 'Four'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    questions     = []
    
    with open('./data/islands/who_owns_these_islands_questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/islands/who_owns_these_islands_questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer  = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/islands/islands_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/islands/islands_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False

            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/islands/islands_leaders.txt'
                               , str(todays_date) + ':'
                               + islands_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect('islands_completed_quiz')

    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = islands_username
                           )


# -----------------------------------------#
# Read   islands_leaders.txt file         #
#        islands_correct_answer.txt       #
#        islands_incorrect_answer.txt     #
# Render islands_quiz_completed.html page #
# -----------------------------------------#
@app.route('/islands_completed_quiz', methods=['GET', 'POST'])
def islands_completed_quiz():  
    
    catname  = 'Islands'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    
    last_count, last_date, last_score, last_username = get_last_line('./data/islands/islands_leaders.txt') 
    correct_answers   = split_answer_file('./data/islands/islands_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/islands/islands_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )

                          
# ----------------------#
# leaderboard category #
# ----------------------#
@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    
    capitals_leaders   = get_leaders_file('./data/capitals/capitals_leaders.txt')
    geography1_leaders = get_leaders_file('./data/geography1/geography1_leaders.txt')
    geography2_leaders = get_leaders_file('./data/geography2/geography2_leaders.txt')
    highest_leaders    = get_leaders_file('./data/highest/highest_leaders.txt')
    islands_leaders    = get_leaders_file('./data/islands/islands_leaders.txt')
    populous_leaders   = get_leaders_file('./data/populous/populous_leaders.txt')
    return render_template('leaders.html',capitals_leaders   = capitals_leaders, 
                                          geography1_leaders = geography1_leaders, 
                                          geography2_leaders = geography2_leaders,
                                          highest_leaders    = highest_leaders,
                                          islands_leaders    = islands_leaders,
                                          populous_leaders   = populous_leaders)  
 
    
# -----------------------------------#
# Get Username for populous category #
# -----------------------------------#
@app.route('/populous_get_username', methods=['GET', 'POST'])
def populous_get_username():

    catname  = 'Populous'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    message  = []
    player   = []
    urlname  = '/populous_get_username'
    urlforname = '/populous_sign_in'

    if request.method == 'POST':
        with open('./data/populous/populous_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                message = "username taken"
            else: 
                file = open('./data/populous/populous_username.txt', 'a')
                file.write(player + '\n') 
                open('./data/populous/populous_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/popolous/populous_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt
                return redirect(url_for('populous_user'))
    return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)   
    

# -------------------------------#
# Sign in for populous category #
# -------------------------------#
@app.route('/populous_sign_in', methods=['GET', 'POST'])
def populous_sign_in():
    
    catname  = 'Populous'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    message  = []
    player   = []
    urlname  = '/populous_sign_in'
    urlforname = '/populous_get_username'
    
    if request.method == 'POST':
        with open('./data/populous/populous_username.txt', 'r') as username_list:
            active_username = username_list.read().splitlines() 
            player = request.form['get_username'].lower() 
            if player in active_username:
                open('./data/populous/populous_correct_answer.txt', 'w').close()   # Create correct_answers.txt 
                open('./data/populous/populous_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt 
                return redirect(url_for('populous_user', populous_username = request.form['get_username']))   
            else:
                message = "Sorry, this username is incorrect. New User?"    
    return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player)    
    
    
# -----------------------------------#
# Read   populous jsonfile          #
# Render populous_quiz.html page    #
# -----------------------------------#
@app.route('/populous_user<populous_username>', methods=['GET', 'POST'])
def populous_user(populous_username):

    catname       = 'populous'
    catnum        = 'Three'
    cattext       = 'Can you choose the LEAST POPULOUS neighbour of countries with exactly three land bordering countries'
    check_correct = []
    imgname       = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    questions     = []
    
    with open('./data/populous/least_populous_of_the_three_questions.json', 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        count_questions  = count_my_question_numbers('./data/populous/least_populous_of_the_three_questions.json')
        todays_date      = create_date()

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer  = questions[index]['answer'] 
            username_answer = request.form['username_answer'].title()
            question_number = questions[index] ["question_number"] 
            
            if username_answer == correct_answer:
                write_to_file('./data/populous/populous_correct_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/populous/populous_incorrect_answer.txt', 'Q' + str(question_number) + ':' + username_answer + '\n') 
                index += 1
                score = score
                check_correct = False

            # When all questions have been answered, save final score #
            if index == count_questions:  # Total number of questions for category
                write_to_file('./data/populous/populous_leaders.txt'
                               , str(todays_date) + ':'
                               + populous_username + ':'
                               + str(count_questions) + ':'
                               + str(score) + '\n') 
                return redirect('populous_completed_quiz')

    return render_template('quiz.html',
                            category = catname,
                            category_text = cattext,
                            catnum = catnum,
                            img_id = imgname,
                            questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = populous_username
                           )    

                           
# -----------------------------------------#
# Read   populous_leaders.txt file         #
#        populous_correct_answer.txt       #
#        populous_incorrect_answer.txt     #
# Render populous_quiz_completed.html page #
# -----------------------------------------#
@app.route('/populous_completed_quiz', methods=['GET', 'POST'])
def populous_completed_quiz():  
    
    catname  = 'Populous'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    
    last_count, last_date, last_score, last_username = get_last_line('./data/populous/populous_leaders.txt') 
    correct_answers   = split_answer_file('./data/populous/populous_correct_answer.txt')
    incorrect_answers = split_answer_file('./data/populous/populous_incorrect_answer.txt')
     
    return render_template("completed_quiz.html", 
                            category = catname,
                            img_id = imgname,
                            last_count = last_count, 
                            last_score = last_score, 
                            incorrect_answers = incorrect_answers, 
                            correct_answers = correct_answers, 
                            last_username = last_username
                          )

                          
if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)  