import os                  # Using operating system dependent functionality.
from flask import Flask    # From module flask import class Flask.

app = Flask(__name__)      # Construct an instance of Flask class for our webapp.

# Route Decorator
@app.route('/')            # URL '/' to be handled by main() route handler.
                           # '/' navigates to localhost:5000.
def hello():               # define function that returns "Hello World".
    return "Hello Flask"
if __name__ == '__main__': # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system. 
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # # Enable reloader and debugger.p