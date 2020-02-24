# Practical Python Milestone 3 Project

## [Riddle-Me-This Guessing Game](https://practical-python-project.herokuapp.com/)

This is the milestone project that I have created for the **“Practical Python”** module, which is part of  “Full Stack Web Development Course” offered by Code Institute.

## Project Brief
This project will be built using logic driven application technologies which have been learnt within the Practical Python module.

* A web application game will ask players to answer questions based on a pictorial or text-based-riddle.
* Players will enter their answer into a text area and submit their answers via a form.
* if a player guesses the answer correctly, They are then asked to answer the next question, If guessed incorrectly, Their incorrect answer is stored and then printed below the riddle, The text area is cleared so they can guess again.
* Multiple players can play the game at the same time within their own browser.
* Players will be identified by their own unique usernames when they log into the game.
* A leader board will show the scores of players ranking them from highest to lowest.

### My Project Overview
A web application game with questions about world geography, questions for the game have been gathered from the following website [**sporcle.com**](https://www.sporcle.com/type/multiplechoice/geography/), As I am creating a question based game I took the option to not give the player(s) the option of guessing the question again as its based on questions rather than riddles.

* The player has a choice of the following six categories  
  * **Geography 1 ?** (18 Questions)
  * **Geography 2 ?** (18 Questions)
  * **Least Populous Of The Three ?** (27 Questions)
  * **Odd One Out Capitals ?** (18 Questions)
  * **Who Owns These Islands ?** (20 Questions)
  * **Which City has the highest elevation above sea level ?** (20 Questions)

## UX  

### Who is this website for ?  
* A website with questions about geography to test knowledge on world geography.

### What is it they want to achieve ?
* To provide a game that player(s) can log into, and then be able to play by answering a series of questions. If a question is answered incorrectly, the game will respond saying the answer was incorrect and continue to the next question.
* The player's score will be incremented each time the question is answered correctly.  When the game has been completed, The player(s) can then see their final score (showing correct & incorrectly answered questions.
* A leaderboard option will show the scores of players ranking them from highest to lowest.

The player must be able to
   1. Use a unique username to play the game.
   2. Be able to answer a pictorial or text-based-riddle question by typing in there answer.
   3. Check there answer and provides feedback to them about their answer.
   4. Be asked the next question in a series of questions.
   5. Be able to play the game again if desired.

### How the project is best way to achieve these things ?
   1.  A way for users to create a unique username via a login facility.
   2.  A source of questions to ask.
   3.  A text area and submit button for the player to enter their answer via a form.
   4.  A logic driven process to check the player's answer for a question, and provide feedback, if the answer is correct or   incorrect.
   5.  Increment the score by one for correct answers.    
   6.  Show a leader board with the scores / ranking from other players.
   7.  Allow multiple players to be able to play game at same time.

### Project Game Planning & Wireframe Mockup
Located at **/static/wireframe/My Practical Python Milestone Project Game Planning.pdf**        
Located at **/static/wireframe/My Practical Python Milestone Project Wireframe.pdf**

### Technologies Used
Technologies used in the construction of this project include,  

* [Bootstrap](https://getbootstrap.com/) is a framework for building responsive, mobile-first websites.
* [Cloud9 IDE](https://aws.amazon.com/cloud9/) is a cloud-based integrated development environment (IDE) used as development environment workspace.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) is a simple mechanism for adding style (e.g., fonts, colors, spacing) to Web documents.
* [CsvJson](https://www.csvjson.com/csv2json) Online tool to convert CSV or TSV formatted data to JSON ,  For validating and formatting of JSON Files.
* [Flask Microframework](http://flask.pocoo.org/) is a microframework for Python.
* [Font Awesome](https://fontawesome.com/) is a font and icon toolkit.
* [Git](https://git-scm.com/) open source distributed version control system.
* [GitHub](https://github.com/) is a Web-based hosting service for version control using Git.
* [Heroku](https://www.heroku.com/) lets you deploy, run and manage applications written in Ruby, Node.js, Java, Python, Clojure, Scala, Go and PHP.
* [HTML5](https://www.w3.org/TR/html52/): is code that describes web pages.
* [JavaScript](https://www.javascript.com/) Javascript is a dynamic computer programming language. And most commonly used as a part of web pages
* [Natsort](https://natsort.readthedocs.io/en/master/) Simple yet flexible natural sorting in Python
* [Pencil](https://pencil.evolus.vn/) is an open-source GUI prototyping tool used to create Wireframe mockup.
* [Python 3.4.3](https://www.python.org/) is a scripting language. updated to `3.6.6`
* [Slack](https://code-institute-room.slack.com/messages) Slack is a collaboration hub that connects your organization
* [StartBootstrap](https://startbootstrap.com/) Free Bootstrap themes and templates.

### Install Flask
1. Install Flask Framework into your workspace in Cloud9 by typing the following command,     
   `sudo pip3 install Flask`  
    Once installed you will see the following message in the Terminal Window.  
    `Successfully installed Flask Jinja2 itsdangerous click Werkzeug MarkupSafe`  
    Then Type in the following command     
    `sudo pip3 freeze --local`  
    This will show the packages and Versions that Flask has installed,   
    `Click==7.0`   
    `Jinja2==2.10` updated to `2.10.1`   
    `MarkupSafe==1.1.0` updated to `1.1.1`  
    `Werkzeug==0.14.1` updated to `0.15.5`   
    `itsdangerous==1.1.0`

### Create run.py file

The following basic Flask application file (run.py) was created in the Cloud9 environment.

```python
import os                  # Using operating system dependent functionality.
from flask import Flask    # From module flask import class Flask.

app = Flask(__name__)      # Construct an instance of Flask class for our webapp.

# Route Decorator
@app.route('/')            # URL '/' to be handled by main() route handler.
                           # '/' navigates to localhost:5000.
def hello():               # define function that returns "Hello World".
return "Hello Flask"
if __name__ == '__main__': # __name__ will be equal to "__main__"S

# If conditional statement is satisfied
app.run(host=os.environ.get('IP'), # launches the Flask's built-in development web server.  
                                   # host=os.environ.get('IP') gets IP Adress from operating system.
port=int(os.environ.get('PORT')),  # os.environ.get('PORT') gets PORT we want to open.
debug=True)                        # # Enable reloader and debugger.
```

Run **run.py** to check that setup and minimal flask application runs ok in Cloud9 environment.  
Click **Run** button and your see the following in the terminal window.  
Note: That Warning message is due to debug=True

```python
Your code is running at https://practical-python-project-bennettpe.c9users.io.
Important: use os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in your scripts!

* Serving Flask app "run" (lazy loading)
* Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead. 
* Debug mode: on
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 381-125-642
```

Click on the https://practical-python-project-bennettpe.c9users.io. and your should see the following in your browser which confirms everything is running OK.   
` Hello Flask `

### Downloading Bootstrap Theme
I decide to download and use the following free one page bootstrap theme (Creative) from [StartBootstrap](https://startbootstrap.com/template-overviews/creative/)

1. Right click on the **Download** Button.
2. Click on **Copy link address**
3. In Cloud9 environment Create a folder called **static**.  
4. In terminal window type **cd static/**
5. Then type **wget** and then paste copied Copy link address as below,
 
    ` $ wget https://github.com/BlackrockDigital/startbootstrap-creative/archive/gh-pages.zip `

6. The following zipped file will be saved in the static directory.
7. Type **unzip gh-pages.zip** which will UnZip the file.
8. The following directory will be created **startbootstrap-creative-gh-pages**
9. Type ````mv startbootstrap-creative-gh-pages/css startbootstrap-creative-gh-pages/img startbootstrap-creative-gh-pages/js startbootstrap-creative-gh-pages/scss startbootstrap-creative-gh-pages/vendor .````
which will Move the files needed into the following file directories CSS,IMG,JS,SCSS,VENDOR
10. Type ````rm -rf startbootstrap-creative-gh-pages ```` to delete unwanted files etc.
11. Type ```` rm gh-pages.zip ```` to deleted unwanted zip file.

### Styling My Templates
Once the Bootstrap theme has been down loaded I needed to edit my templates so it picked up the downloaded theme correctly.

1. Go to the github page of the theme (Creative) https://github.com/BlackrockDigital/startbootstrap-creative
2. Copy the **link** and **script** lines from **index.html** into **base.html** and amend directory locations.
3. Copied rest of **index.html** code into **base.html**
4. Created **index.htm** and added the following code

```
{% extends 'base.html' %}
{% block content %}
{% endblock %}
```

### Cloud9 File directory structure
The following file directory structure was created in the Cloud9 environment.

```
├── data                 # Quiz Data files (Each category contains these txt files)
│   ├── capitals
│   │   ├── capitals_correct_answers.txt
│   │   ├── capitals_incorrect_answers.txt
│   │   ├── capitals_leaders.txt
│   │   └── capitals_username.txt
│   │
│   ├── geography1
│   ├── geography2
│   ├── highest
│   ├── islands
│   └── populous
│   
├── static
│   ├── css                    # Bootstrap files
│   ├── images                 # Quiz category image files
│   │   ├── Geography1
│   │   ├── Geography2
│   │   ├── Least Populous Of The Three
│   │   ├── Odd One Out Capitals
│   │   ├── Website
│   │   ├── Which City Has The Highest Elevation Above Sea Level
│   │   └── Who Owns These Islands
│   │
│   ├── img                    # Website category images
│   ├── js                     # Bootstrap files
│   ├── scss                   # Bootstrap files
│   ├── vendor                 # Bootstrap files
│   └── wireframe              # Mockup and Planning files
│    
├── templates                  # html templates
│   ├── base.html
│   ├── completed_quiz.html  
│   ├── footer.html
│   ├── get_username.html
│   ├── head.html
│   ├── leader.html
│   ├── navbar_quiz.html
│   ├── navbar_username.html
│   ├── quiz.html
│   └── script.html
│    
├── READMD.md
├── requirements.txt
├── run.py                   # Python File
├── test_*                   # Manual unit testing file(s)
└── Procfile
```

### Create Json file(s)
The Questions for the game where loaded into **.json** file(s) in the **data** directory folder

```
practical-python-project
└── data                                                                      
    ├── capitals
    │   └── odd_one_out_capitals_questions.json
    ├── geography1
    │   └── geography2_questions.json
    ├── highest
    │   └── which_city_has_the_highest_elevation_above_sea_level_questions.json
    ├── islands
    │   └── who_owns_these_islands_questions.json
    └── populous
        └── least_populous_of_the_three_questions.json
```

The **.json** file(s) were created as follows   

1. CSV files created with the following Column variables
```
    question_number,question,option_a,option_b,option_c,option_d,answer,answer_letter,image_source
```

`Least Populous Of The Three ?` and `Which City has the highest elevation above sea level ?` categories only have three multiple choice options.  

2. These files(s) were then converted to a **.json** file(s) and validated using the following tool [CsvJson](https://www.csvjson.com/csv2json)   

### Testing
The project guidelines stated that a Test Driven Development (TDD) approach should be taken to developing the game, But all of my testing / bug fixes was done from a manual testing approach using print() method ,Building some test* python code when I wanted to create a new piece of logic / functionality or had a issue.

#### Manual Testing
1. After styling my templates I ran **run.py** to make sure it worked OK had a couple of issues, highlighted in (Bugs and Issues > Development Testing > 1.) which were fixed.   

2. After building leaders html page I ran **test_get_leaders_score.py** and noticed the sorted order was incorrect and it showed score of 9 before 10,highlighted in (Bugs and Issues > Development Testing > 2.) which were fixed.

```python    
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
```
3. Before building sign_in html page I ran **test_get_username.py** to test username logic.

```python
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
```

#### Responsive screen testing
- I used open source Bootstrap theme (Creative) by [Start Bootstrap](https://startbootstrap.com/) so responsive screen issues should be ok.
- The quiz is responsive and works best on a large to medium screen, horizontally displayed.
- On smaller screens, it works fine, but there is a small amount of scrolling on the 'Quiz answer options 1,2,3,4' and the 'Questions correct vs incorrect section' which I am going to see if I can improve. 
- I have now fixed the scrolling issue on the 'Questions correct vs incorrect section' by adding `padding-left: 5px;` in CSS file and removing `col-lg-4 col-sm-6 mx-auto` from the **completed_quiz.html** file

#### Bugs and Issues
##### Development Testing
1. Had an issues when styling my templates,
	* Images not being displayed  
Had not amended directory location for **.jpg** files changed `img/portfolio` to `static/img/portfolio`
	* Font awesome icons not being displayed,
Had missing ending **"** on link.

2. Had an issues when sorting leaders txt files,
    * When trying to sort by scores it was ordering score 9 before 10 this was due to python sort order and needed to be changed to natural sort order.
    * Installed **natsort** (see below)
    * Updated python code in function `def get_leaders_file(filename):` as follows:     
 
	```python
	# natural sort , highest first, top 6
	return natsorted(sorted_players,key=sortkey,reverse=True)[:6]
	```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Installing Natsort**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Install Natsort into your workspace in Cloud9 by typing the following command,     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sudo pip3 install natsort`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Once installed you will see the following message in the Terminal Window.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `Successfully installed natsort`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Then Type in the following command     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `sudo pip3 freeze --local > requirements.txt`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This will show the packages and Versions that Natsort has installed, and these have been copied <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; to the **requirements.txt file**. 

```python
		Click==7.0
        Flask==1.0.2
        Flask-DebugToolbar==0.10.1
        Flask-Testing==0.7.1
        Jinja2==2.10.1
        MarkupSafe==1.1.1
        Werkzeug==0.15.5
        blinker==1.4
        itsdangerous==1.1.0
        natsort==7.0.1
``` 
 
1. The refactoring of the ***_quiz.html**, caused a issue as the Highest & Populous categories have 3 questions instead of 4 so the 4th question were showing up as blank, it was fix as follows:
`catnum=Three` for 3 questions and `catman=Four` for 4 questions in the quiz sections of the **run.py**

	```python
    catnum  = 'Three' # if three questions
    catnum  = 'Four'  # if four questions
	```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In the **quiz.html** code the following was added so the fourth question would be shown if  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`catnum == Four`

```python
{% if catnum == 'Four' %}
	<span class="text-dark"> 4. <span class="text-light"> {{ questions[index]["option4"] }} </span>
{% endif %}
```

4. The registering and signing in for usernames , I had not added anything to check for duplicate usernames so added the following code for each category.

* Run.py   
This code checks the ***_username.txt** file to see if the username has previously been entered, If so message is shown in **get_username.html** to highlight this and you are asked to enter a new username, if you have already registered then you are asked to sign-in, if its a new username then you are taken to the sign-in page.

```python
urlname    = '/capitals_get_username'
urlforname = '/capitals_sign_in'

if request.method == 'POST':
    with open('./data/capitals/capitals_username.txt', 'r') as username_list:
        active_username = username_list.read().splitlines()
        player = request.form['get_username'].lower()
        if player in active_username:
            message = "USERNAME taken"
        else:
            file = open('./data/capitals/capitals_username.txt', 'a')
            file.write(player + '\n')  
            open('./data/capitals/capitals_correct_answer.txt', 'w').close()   # Create correct_answers.txt
            open('./data/capitals/capitals_incorrect_answer.txt', 'w').close() # Create incorrect_answers.txt
        return redirect(url_for('capitals_sign_in'))  
return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, username_message=message, username_player=player)  
```   
This is the code for the sign-in section which asked you to enter the username and then takes you to the category questions page. if you input a username which is not in the username text file a message is shown asking if you have already registered, with a link back to the registration section.  

```python
# --------------------------------#
# Sign in  for capitals category #
# --------------------------------#
@app.route('/capitals_sign_in', methods=['GET', 'POST'])
def capitals_sign_in():

catname    = 'Odd One Out Capitals'
imgname    = './static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
urlname    = '/capitals_sign_in'
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
        message = "Sorry, this USERNAME is incorrect. New User?"    
return render_template('sign_in.html',category=catname, img_id=imgname, url_id=urlname, urlforname=urlforname, signin_message=message, username_player=player)  
```    
    
5. I had not added code as per project brief for the following: `Multiple players can play the game at the same time within their own browser`, so needed to add Flask Sessions to be able to achieve this,    
But apparently there where no video's in section 7. Practical Python for this so used the following you tube video's to understand about flask sessions [Flask Session](https://www.youtube.com/watch?v=T1ZVyY1LWOg)  
After discussing the issue in slack Practical Python thread , apparently the flask mini project video's have been amended on the 05/12/18 to include information on sessions.

    Secret Key and `from flask import session` had to be added to allow flask sessions to be used ,the secret key was generated using the following code

```python
    # How to generate a secret key with Python
    # via http://flask.pocoo.org/docs/quickstart/
    import os
    print(os.urandom(16))
```

### Refactoring

#### *_get_username.html
1. I have made changes to the **get_username** processing as follows which reduces the number of HTML templates from one per question category to one for all categories (**get_username.html**) so I could then delete the unwanted HTML templates.

        deleted:    templates/capitals_get_username.html
        deleted:    templates/geography1_get_username.html
        deleted:    templates/geography2_get_username.html        
        deleted:    templates/highest_get_username.html
        deleted:    templates/islands_get_username.html
        deleted:    templates/populous_get_username.html

    Changed from this

```python
username_list.write(request.form['capitals_username']+ '\n')  
return redirect(url_for('capitals_user', capitals_username = request.form['capitals_username']))
return render_template('capitals_get_username.html',category=catname, img_id=imgname)
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changed to this

```python
urlname  = '/capitals_get_username'
username_list.write(request.form['get_username']+ '\n')
return redirect(url_for('capitals_user', capitals_username = request.form['get_username']))     
return render_template('get_username.html',category=catname, img_id=imgname, url_id=urlname)   
```

#### *_quiz.html
2. I have made changes to the **quiz** processing as follows which reduces the number of HTML templates from one per question category to one for all categories (**get_usernamequiz.html**) so I could then delete the unwanted HTML templates.

        deleted:    templates/capitals_quiz.html
        deleted:    templates/geography1_quiz.html
        deleted:    templates/geography2_quiz.html
        deleted:    templates/highest_quiz.html
        deleted:    templates/islands_quiz.html
        deleted:    templates/populous_quiz.html

    Changed from this

```python
    return render_template('capitals_quiz.html',
    capitals_questions = questions,
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Changed to this

```python       
    cattext  = 'Can you choose the capital that is NOT on the given continent'
    return render_template('quiz.html',
    category_text = cattext,
    capitals_questions = questions,
```

#### get_username.html
3. I have made changes to the **get_username.html** so that the `Register Username` & `Sign-in` links are on the same html page rather than clicking button `Register Username` which if already register would then give you a link to the `sign_in.html` page.

## Deployment Instructions
##### Instructions for deploying Python app onto a hosing site: [Heroku](https://www.heroku.com/) hosing site

If you have not Signed up to Heroku then you need to start from **Signing Up To Heroku** , otherwise start from **In Heroku (Part One)**

1. **Signing Up To Heroku**
      1.  Sign up to [Heroku](https://id.heroku.com/login)
      2.  Click on New to Heroku? `Sign Up` at the bottom of the Log in to your account panel.
      3.  Complete the Form by entering your details as required and in 'Primary Development Language Box' Enter `Python`.
      4.  After completing the
      Form your will receive a 'Verification Email', which can take up to 15 minutes to receive.
      5. Open the 'Verification Email' and click on the link and you will be prompted to Enter a password and click `Here To Proceed button`.

2. **Heroku Checklist**

	  The following needs to be created
      - Create a requirements.txt file.
      - Create a Procfile file.
      - Create a new Heroku app.
      - Create any Config variables.
      - Push the code to Heroku.

3. **In Heroku (Create app)**
      1. **Log in** to [Heroku](https://id.heroku.com/login)
      2. Select **New** and **Create new app**.
      3. Create **App name** > Select **Choose a region** > Then **Create app**.

4. **From Cloud9 (Readying for deployment)**
	1. Making the **run.py** file ready for deployment  
	
		We need to make the secret key an environment variable and its going to look for a variable called `SECRET` , the 2nd argument is the default value if Flask cannot find the variable called SECRET, so we apply the following changes in the app.secret_key method.

```python
 app.secret_key = os.getenv("SECRET", "b'\xa0\xba+\xe5\xaa\x8b\xac\x01\x96\x1f<)86\x84\x04")
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We need to add these default fallback values to our IP and port in the app.run() method, so we &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; add `0.0.0.0` for the IP and `5000` for the port and then we won't have to set these in Heroku, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; also we set `debug=True` to `debug=False` in production.

```python
app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT","5000")), debug=false )
```

2. Type in the following command in the terminal window, which creates the **Procfile file** (Remember to use a capital P in Procfile).   
     `echo web: python run.py > Procfile`  
        The **Procfile** file contains `web: python run.py` which tells Heroku to start a process called web and to run `python run.py` when it starts.
	3. Type in the following command in the terminal window, which creates the pip **requirements.txt file**.   `sudo pip3 freeze --local > requirements.txt`  
       The **requirements.txt** file contains a list of items to be installed, defining the modules imported to Heroku:      
	4. Type in the following command in the terminal window which adds all project files: `$ git add .`
	5. Type in the following command in the terminal window to create a default message for the first 		commit to Heroku: `$ git commit -m "Added Procfile for deployment"`
	6. Type in the following command into the terminal window to run the heroku login command `$ heroku login`
	7. Type into the terminal window your email address and password.
	8. Type into the terminal window `$ git remote -v` Heroku references have already been added.
	9. Now you are logged into Heroku you need to create a new heroku app by typing the following command `$ heroku apps:create my-practical-python-project`,once created it will also give us a git address as well.
	10. Before we push our app to Heroku we need to set our environment variables `https://dashboard.heroku.comm/apps`

5. **In Heroku (Config vars)**
      1. Refresh the Heroku dashboard and you should see your new heroku app `my-practical-python-project` has been created, Click on that and then go to `Settings` > `Reveal Config Vars`, at the moment we don't have any config vars.
      2. So in the Key field enter `SECRET` and in the Value field enter `b'\xa0\xba+\xe5\xaa\x8b\xac\x01\x96\x1f<)86\x84\x04` and then click on Add Button.  

6. **In Cloud9 (Build the source)**
      1. Once that's gone we can Push the project to Heroku so we go back into cloud9 terminal window and type the following command  `$ git push -u heroku master` this will build the source and then install everything from the requirements.txt file, watch the installation log for error.
      This has now deployed our app to Heroku.

7. **In Heroku (Open app)**    
     1. Click Open app  
     Select new tab, [my practical python project](https:// my-practical-python-project.herokuapp.com/)

### Credits

#### Content

#### Media
- Background image for Top of website taken from [pixabay](https://cdn.pixabay.com/photo/2015/01/15/16/17/hands-600497_960_720.jpg)
- The Six background Images used for **‘Quiz Selection Section’** of website where taken from [Rawpixel](https://www.rawpixel.com/).
- All Images in categories taken from [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page)

#### Acknowledgements
- I would like to thank my fellow students for their help with my (Advice, Bug fixing, Issues, Queries) via [Slack](https://code-institute-room.slack.com/messages)
- I would also like to thank my Code Institute Mentor Chris Zielinski (Display name ckz8780_mentor)