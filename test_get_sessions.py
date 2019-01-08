import os
from flask import Flask, session

app = Flask(__name__)

# Key generated from Secretkey.py
app.secret_key = os.urandom(24)

# --------------------------------#
# Route Decorator for index.html #
# --------------------------------#
@app.route('/')
def index():
    session['user'] = 'Paul'
    return 'Index'

@app.route('/getsession')  
def getsession():
    if 'user' in session:
        return session['user']
        
    return 'Not Logged in!'    

@app.route('/dropsession')  
def dropsession(): 
    session.pop('user', None)
    return 'Dropped!'
    

if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)      