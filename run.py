import os                                     # Using operating system dependent functionality.
from flask import Flask                       # From module flask (import class Flask).
from flask import render_template             # From module flask (import class render_template).
from flask import redirect                    # From module flask (import class redirect).
from flask import request                     # From module flask (import class request).
from flask import url_for                     # From module flask (import class url_for).

app = Flask(__name__)                         # Construct an instance of Flask class for our webapp.

# Route Decorator for index
@app.route('/')
def index():
    return render_template('index.html')      # Routing for index.html 

# Route Decorator for geography1 questions    
@app.route('/geography1_get_user')
def geography1_get_user():
    return render_template('geography1_get_user.html', category="Geography 1")               # Routing for geography1_get_user.html
    
# Route Decorator for geography2 questions    
@app.route('/geography2_get_user')
def geography2_get_user():
    return render_template('geography2_get_user.html', category="Geography 2")               # Routing for geography2_get_user.html    
    
# Route Decorator for populous questions    
@app.route('/populous_get_user')
def populous_get_user():
    return render_template('populous_get_user.html', category="Least Populous Of The Three") # Routing for populous_get_user.html   
    
# Route Decorator for capitals questions    
@app.route('/capitals_get_user')
def capitals_get_user():
    return render_template('capitals_get_user.html', category="Odd One Out Capitals")        # Routing for capitals_get_user.html       

# Route Decorator for islands questions    
@app.route('/islands_get_user')
def islands_get_user():
    return render_template('islands_get_user.html', category="Who Owns These Islands")        # Routing for islands_get_user.html   

# Route Decorator for highest questions    
@app.route('/highest_get_user')
def highest_get_user():
    return render_template('highest_get_user.html', category="Which City Is Highest")         # Routing for highest_get_user.html   
    
if __name__ == '__main__':                    # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # Enable reloader and debugger.p