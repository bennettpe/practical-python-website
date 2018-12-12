import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

    
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
    
    
# --------------------------#
# Writing to file function #
# --------------------------#
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)    


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

    if request.method == 'POST':
        with open('./data/capitals/capitals_username.txt', 'a') as username_list:
             username_list.write(request.form['capitals_username']+ '\n')  
        open('./data/capitals/capitals_correct_answer.txt', 'w').close()  
        open('./data/capitals/capitals_incorrect_answer.txt', 'w').close()
        return redirect(url_for('capitals_user', capitals_username = request.form['capitals_username']))
    return render_template('capitals_get_username.html',category=catname, img_id=imgname)
    
# -----------------------------------#
# Read   capitals jsonfile          #
# Render capitals_quiz.html page    #
# -----------------------------------#
@app.route('/capitals_user<capitals_username>', methods=['GET', 'POST'])
def capitals_user(capitals_username):

    catname  = 'Odd One Out Capitals'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('capitals_completed_quiz')


    return render_template('capitals_quiz.html',
                            category = catname,
                            img_id = imgname,
                            capitals_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = capitals_username
                           )    
  
                           
# --------------------------------------#
# Get Username for geography1 category #
# --------------------------------------#
@app.route('/geography1_get_username', methods=['GET', 'POST'])
def geography1_get_username():

    catname  = 'Geography 1'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'

    if request.method == 'POST':
        with open('./data/geography1/geography1_username.txt', 'a') as username_list:
             username_list.write(request.form['geography1_username']+ '\n')  
        open('./data/geography1/geography1_correct_answer.txt', 'w').close()  
        open('./data/geography1/geography1_incorrect_answer.txt', 'w').close()
        return redirect(url_for('geography1_user', geography1_username = request.form['geography1_username']))
    return render_template('geography1_get_username.html',category=catname, img_id=imgname)


# -------------------------------------#
# Read   geography1 jsonfile          #
# Render geography1_quiz.html page    #
# -------------------------------------#
@app.route('/geography1_user<geography1_username>', methods=['GET', 'POST'])
def geography1_user(geography1_username):

    catname  = 'Geography 1'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('geography1_completed_quiz')


    return render_template('geography1_quiz.html',
                            category = catname,
                            img_id = imgname,
                            geography1_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = geography1_username
                           )

                           
# --------------------------------------#
# Get Username for geography2 category #
# --------------------------------------#
@app.route('/geography2_get_username', methods=['GET', 'POST'])
def geography2_get_username():

    catname  = 'Geography 2'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'

    if request.method == 'POST':
        with open('./data/geography2/geography2_username.txt', 'a') as username_list:
            username_list.write(request.form['geography2_username']+ '\n')  
        open('./data/geography2/geography2_correct_answer.txt', 'w').close()  
        open('./data/geography2/geography2_incorrect_answer.txt', 'w').close()
        return redirect(url_for('geography2_user', geography2_username = request.form['geography2_username']))
    return render_template('geography2_get_username.html',category=catname, img_id=imgname)


# -------------------------------------#
# Read   geography2 jsonfile          #
# Render geography2_quiz.html page    #
# -------------------------------------#
@app.route('/geography2_user<geography2_username>', methods=['GET', 'POST'])
def geography2_user(geography2_username):

    catname  = 'Geography 2'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('geography2_completed_quiz')


    return render_template('geography2_quiz.html',
                            category = catname,
                            img_id = imgname,
                            geography2_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = geography2_username
                           )

# -----------------------------------#
# Get Username for highest category #
# -----------------------------------#
@app.route('/highest_get_username', methods=['GET', 'POST'])
def highest_get_username():

    catname  = 'Highest'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'

    if request.method == 'POST':
        with open('./data/highest/highest_username.txt', 'a') as username_list:
             username_list.write(request.form['highest_username']+ '\n')  
        open('./data/highest/highest_correct_answer.txt', 'w').close()  
        open('./data/highest/highest_incorrect_answer.txt', 'w').close()
        return redirect(url_for('highest_user', highest_username = request.form['highest_username']))
    return render_template('highest_get_username.html',category=catname, img_id=imgname)


# ----------------------------------#
# Read   highest jsonfile          #
# Render highest_quiz.html page    #
# ----------------------------------#
@app.route('/highest_user<highest_username>', methods=['GET', 'POST'])
def highest_user(highest_username):

    catname  = 'Highest'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('highest_completed_quiz')


    return render_template('highest_quiz.html',
                            category = catname,
                            img_id = imgname,
                            highest_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = highest_username
                           )
                           
                           
# -----------------------------------#
# Get Username for islands category #
# -----------------------------------#
@app.route('/islands_get_username', methods=['GET', 'POST'])
def islands_get_username():

    catname  = 'Islands'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'

    if request.method == 'POST':
        with open('./data/islands/islands_username.txt', 'a') as username_list:
             username_list.write(request.form['islands_username']+ '\n')  
        open('./data/islands/islands_correct_answer.txt', 'w').close()  
        open('./data/islands/islands_incorrect_answer.txt', 'w').close()
        return redirect(url_for('islands_user', islands_username = request.form['islands_username']))
    return render_template('islands_get_username.html',category=catname, img_id=imgname)


# ----------------------------------#
# Read   islands jsonfile          #
# Render islands_quiz.html page    #
# ----------------------------------#
@app.route('/islands_user<islands_username>', methods=['GET', 'POST'])
def islands_user(islands_username):

    catname  = 'Islands'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('islands_completed_quiz')


    return render_template('islands_quiz.html',
                            category = catname,
                            img_id = imgname,
                            islands_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = islands_username
                           )
                           
                           
# -----------------------------------#
# Get Username for populous category #
# -----------------------------------#
@app.route('/populous_get_username', methods=['GET', 'POST'])
def populous_get_username():

    catname  = 'Populous'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'

    if request.method == 'POST':
        with open('./data/populous/populous_username.txt', 'a') as username_list:
             username_list.write(request.form['populous_username']+ '\n')  
        open('./data/populous/populous_correct_answer.txt', 'w').close()  
        open('./data/populous/populous_incorrect_answer.txt', 'w').close()
        return redirect(url_for('populous_user', populous_username = request.form['populous_username']))
    return render_template('populous_get_username.html',category=catname, img_id=imgname)
    
    
# -----------------------------------#
# Read   populous jsonfile          #
# Render populous_quiz.html page    #
# -----------------------------------#
@app.route('/populous_user<populous_username>', methods=['GET', 'POST'])
def populous_user(populous_username):

    catname  = 'populous'
    imgname  = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    check_correct = []
    questions = []
    
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
                               + request.form['score'] + '\n')  
                return redirect('populous_completed_quiz')


    return render_template('populous_quiz.html',
                            category = catname,
                            img_id = imgname,
                            populous_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            username = populous_username
                           )    

if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)  