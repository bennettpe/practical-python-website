import os
from datetime import datetime
from flask import Flask, flash, json, render_template, redirect, request, url_for

app = Flask(__name__)
# Key generated from Secretkey.py
app.secret_key = "b'\xa0\xba+\xe5\xaa\x8b\xac\x01\x96\x1f<)86\x84\x04" 


# ------------------------ #
# Writing to file process #
# -------------------------#

def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)


# ------------------------------- #
# Count question_numbers process #
# --------------------------------#

def count_my_question_numbers():
    with open('./data/geography1/geography1_questions.json', 'r') as json_data:
        data = json.load(json_data)
    return len(data)


# -------------------- #
# Create date process #
# ---------------------#

def create_date():
    date_format = '%d/%m/%y'
    get_date = datetime.now().strftime(date_format)
    return get_date


# --------------------------------#
# Route Decorator for index.html #
# --------------------------------#

@app.route('/')
def index():
    return render_template('index.html')


# ---------------------------#
# Get last incorrect answer #
# ---------------------------#

def get_geography1_incorrect_answer():
    answers = []
    with open('./data/geography1/geography1_incorrect_answer.txt', 'r') as incorrect_answer:
        answers = [row for row in incorrect_answer]
        return answers[-1:]


# --------------------------------------#
# Get Username for geography1 category #
# --------------------------------------#

@app.route('/geography1_get_username', methods=['GET', 'POST'])
def geography1_get_username():

    catname = 'Geography 1'
    filename = './data/geography1/geography1_username.txt'
    imgname = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'

    if request.method == 'POST':
        with open(filename, 'a') as username_list:username_list.write(request.form['geography1_username']+ '\n')  
        return redirect(request.form['geography1_username'])

        open('./data/geography1/geography1_correct_answer.txt', 'w').close()  
        open('./data/geography1/geography1_incorrect_answer.txt', 'w').close()
        open('./data/geography1/geography1_final_score.txt', 'w').close()
    return render_template('geography1_get_username.html',category=catname, img_id=imgname)


# -------------------------------------#
# Read   geography1 jsonfile          #
# Render geography1_quiz.html page    #
# -------------------------------------#

@app.route('/<geography1_username>', methods=['GET', 'POST'])
def geography1_user(geography1_username):

    catname = 'Geography 1'
    filename = './data/geography1/geography1_questions.json'
    imgname = './static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    check_correct = []
    questions = []

    with open(filename, 'r') as questions_file:  
        questions = json.load(questions_file)

        index = 0
        score = 0
        correct_answer = questions[index]['answer']
        count_questions = count_my_question_numbers()
        incorrect_answer = get_geography1_incorrect_answer()
        todays_date = create_date()

        open('./data/geography1/geography1_correct_answer.txt', 'a')  
        open('./data/geography1/geography1_incorrect_answer.txt', 'a')
        open('./data/geography1/geography1_final_score.txt', 'a')

        if request.method == 'POST':
            index = int(request.form['index'])
            score = int(request.form['score'])
            correct_answer = request.form['correct_answer']
            username_answer = request.form['username_answer'].title()

            if username_answer == correct_answer:
                write_to_file('./data/geography1/geography1_correct_answer.txt'
                              , username_answer + '\n') 
                index += 1  
                score += 1
                check_correct = True
            else:
                write_to_file('./data/geography1/geography1_incorrect_answer.txt'
                              , username_answer + '\n') 
                index += 1
                score = score
                check_correct = False

            # When all questions have been answered, save final score in geography1_leaders.txt #

            if request.method == 'POST':
                if index == 18:  # Total number of questions for category
                    write_to_file('./data/geography1/geography1_leaders.txt'
                                  , str(todays_date) + ':'
                                  + geography1_username + ':'
                                  + str(count_questions) + ':'
                                  + request.form['score'] + '\n')  
                    write_to_file('./data/geography1/geography1_final_score.txt'
                                  , request.form['score'] + '\n')  
                    return redirect('geography1_completed_quiz')

    incorrect_answer = get_geography1_incorrect_answer()

    return render_template('geography1_quiz.html',
                            category = catname,
                            img_id = imgname,
                            geography1_questions = questions,
                            index = index,
                            score = score,
                            check_correct = check_correct,
                            correct_answer = questions[index]['answer'],
                            count_questions = count_questions,
                            incorrect_answer = incorrect_answer,
                            username = geography1_username,
                           )


# Route Decorator for geography2 username

@app.route('/geography2_username')
def geography2_username():
    image = \
        'static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'  # Image Filename
    return render_template('geography2_username.html',
                           category='Geography 2', img_id=image)  # Routing for geography2_username.html


# Route Decorator for populous username

@app.route('/populous_username')
def populous_username():
    image = \
        'static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'  # Image filename
    return render_template('populous_username.html',
                           category='Least Populous Of The Three',
                           img_id=image)  # Routing for populous_username.html


# Route Decorator for capitals username

@app.route('/capitals_username')
def capitals_username():
    image = \
        'static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'  # Image filename
    return render_template('capitals_username.html',
                           category='Odd One Out Capitals',
                           img_id=image)  # Routing for capitals_username.html


# Route Decorator for islands username

@app.route('/islands_username')
def islands_username():
    image = \
        'static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'  # Image filename
    return render_template('islands_username.html',
                           category='Who Owns These Islands',
                           img_id=image)  # Routing for islands_username.html


# Route Decorator for highest questions

@app.route('/highest_username')
def highest_username():
    image = \
        'static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'  # Image filename
    return render_template('highest_username.html',
                           category='Which City Is Highest',
                           img_id=image)  # Routing for highest_username.html

if __name__ == '__main__':  # __name__ will be equal to "__main__"

# If conditional statement is satisfied

    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)  