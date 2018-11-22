import os                                     # Using operating system dependent functionality.
from flask import Flask                       # From module flask (import class Flask).
from flask import json                        # From module flask (import class json).
from flask import render_template             # From module flask (import class render_template).
from flask import redirect                    # From module flask (import class redirect).
from flask import request                     # From module flask (import class request).
from flask import session                     # From module flask (import class session).
from flask import url_for                     # From module flask (import class url_for).

app = Flask(__name__)                         # Construct an instance of Flask class for our webapp.

# Route Decorator for index
@app.route('/')
def index():
    return render_template('index.html')      # Routing for index.html 

# Route Decorator for geography1 username    
@app.route('/geography1_username', methods=["GET", "POST"])
def geography1_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-90517.jpg'
    if request.method == 'POST':                                                                            # if request method is 'POST' send data to server
       with open("data/geography1/geography1_username.txt", "a") as username_list:                          # Append USERNAME as username_list
            username_list.write(request.form["geography1_username"] + "\n")                                 # Write  USERNAME to geography1_username.txt   
       return redirect(request.form["geography1_username"])                                                 # Redirect to geography1_username.txt  
    return render_template('geography1_username.html', category='Geography 1', img_id=image)                # Renders template from template folder

# Route Decorator for geography2 username    
@app.route('/geography2_username')
def geography2_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-433915.jpg'
    return render_template('geography2_username.html', category='Geography 2', img_id=image)                # Routing for geography2_username.html    
    
# Route Decorator for populous username    
@app.route('/populous_username')
def populous_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-90625.jpg'
    return render_template('populous_username.html', category='Least Populous Of The Three', img_id=image)  # Routing for populous_username.html   
    
# Route Decorator for capitals username    
@app.route('/capitals_username')
def capitals_username(): 
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-442135.jpg'
    return render_template('capitals_username.html', category='Odd One Out Capitals', img_id=image)         # Routing for capitals_username.html 

# Route Decorator for islands username    
@app.route('/islands_username')
def islands_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-424508.jpg'
    return render_template('islands_username.html', category='Who Owns These Islands', img_id=image)        # Routing for islands_username.html   

# Route Decorator for highest questions    
@app.route('/highest_username')
def highest_username():
    image = 'static/img/portfolio/thumbnails/image-from-rawpixel-id-431844.jpg'
    return render_template('highest_username.html', category='Which City Is Highest', img_id=image)       # Routing for highest_username.html
    
if __name__ == '__main__':                    # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # Enable reloader and debugger.p