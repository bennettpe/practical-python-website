import os                                     # Using operating system dependent functionality.
from flask import Flask, render_template      # From module flask (import class Flask, render_template).

app = Flask(__name__)                         # Construct an instance of Flask class for our webapp.

# Route Decorator
@app.route('/')
def index():
    return render_template("index.html")      # Routing for index.html 
    
if __name__ == '__main__':                    # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # Enable reloader and debugger.p