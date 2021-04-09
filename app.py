
import os  # connects the OS library so we can lookup our own IP address
from flask import Flask, render_template   # this connects our framework of tools we'll need

app = Flask(__name__)  # here we create our app in memory. It's maybe the most important line of code

@app.route('/') # if anyone tries to go to the  homepage, their request will be routed to the method below
def index():
    return render_template('index.html')

if __name__ == '__main__':
    host = os.getenv('IP', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.debug = True 
    app.run(host=host, port=port, debug=True)