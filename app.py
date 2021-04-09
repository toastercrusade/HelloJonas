
import os  # connects the OS library so we can lookup our own IP address
from flask import Flask, render_template, request, jsonify   # this connects our framework of tools we'll need

app = Flask(__name__)  # here we create our app in memory. It's maybe the most important line of code

global current_hs
current_hs = 0

@app.route('/') # if anyone tries to go to the  homepage, their request will be routed to the method below
def index():
    global current_hs
    return render_template('index.html', highscore=current_hs)

## NEW STUFF
@app.route('/update/score', methods=['POST'])
def update_score():
    global current_hs
    try: 
        current_hs = int(request.form['score'])
        return jsonify({'success' : 'Highscore now updated'})
    except:
        return jsonify({'error' : 'Highscore not updated'})

if __name__ == '__main__':
    host = os.getenv('IP', '127.0.0.1')
    port = int(os.getenv('PORT', 5000))
    app.debug = True 
    app.run(host=host, port=port, debug=True)