import os                                     
from flask import Flask, json, render_template, redirect, request, url_for  

app = Flask(__name__)   

#--------------------------------#
# Route Decorator for index.html # 
#--------------------------------#
@app.route('/')
def index():
    return render_template('index.html')                                                            

#--------------------------------------#
# Get Username for geography1 category # 
#--------------------------------------#
@app.route('/geography1_get_username',methods = ['GET', 'POST'])
def geography1_get_username():
    
    catname  = "Geography 1"                                                                       # Catergory Name
    filename = "./data/geography1/geography1_username.txt"                                         # Username Filename 
    imgname  = "./static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg"                # Image Filename
       
    if request.method == 'POST':                                                                   
       with open(filename, "a") as username_list:                                                  
            username_list.write(request.form["geography1_username"] + "\n")                         
       return redirect(request.form["geography1_username"])                                        
    return render_template("geography1_get_username.html", category=catname, img_id=imgname)       
   
#-------------------------------------#   
# Read   geography1 jsonfile          #
# Render geography1_quiz.html page    #
#-------------------------------------#
@app.route('/<geography1_username>',methods = ['GET', 'POST'])                                                  
def geography1_user(geography1_username):                                                   

    catname  = "Geography 1"                                                                        # Catergory Name
    filename = "./data/geography1/geography1_questions.json"                                        # Input Filename
    imgname  = "./static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg"                # Image Filename
    questions =[]  
   
    with open(filename, "r") as questions_file:                                                   
         questions = json.load(questions_file)                                                
         index = 0                                                                       
         score = 0                                                                        
    return render_template("geography1_quiz.html", category=catname, img_id=imgname, username=geography1_username, index=index, geography1_questions=questions)               
     
 
# Route Decorator for geography2 username    
@app.route('/geography2_username')
def geography2_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'                                # Image Filename
    return render_template('geography2_username.html', category='Geography 2', img_id=image)                   # Routing for geography2_username.html    
 
    
# Route Decorator for populous username    
@app.route('/populous_username')
def populous_username(): 
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'                                 # Image filename
    return render_template('populous_username.html', category='Least Populous Of The Three', img_id=image)     # Routing for populous_username.html   

    
# Route Decorator for capitals username    
@app.route('/capitals_username')
def capitals_username(): 
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'                                # Image filename
    return render_template('capitals_username.html', category='Odd One Out Capitals', img_id=image)            # Routing for capitals_username.html 


# Route Decorator for islands username    
@app.route('/islands_username')
def islands_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'                                # Image filename
    return render_template('islands_username.html', category='Who Owns These Islands', img_id=image)           # Routing for islands_username.html   


# Route Decorator for highest questions    
@app.route('/highest_username')
def highest_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'                                # Image filename
    return render_template('highest_username.html', category='Which City Is Highest', img_id=image)            # Routing for highest_username.html

    
if __name__ == '__main__':                    # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # Enable reloader and debugger.p