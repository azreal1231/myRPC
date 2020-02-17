from flask import Flask, jsonify, render_template, request
from random import randint
app = Flask(__name__)






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rpc')
def add_numbers():
    list = \
        [
            "Superman didn't always fly.",
            "Space smells like seared steak.",
            "The longest wedding veil was the same length as 63.5 football fields.",
            "The total weight of ants on earth once equaled the total weight of people.",
            "A dozen bodies were once found in Benjamin Franklin's basement.",
        ]

    r = randint(0, len(list))



    de = request.args.get('de',  type=str)
    params = request.args.get('params',  type=str)

    if de == 'work':
        msg = {'STATUS':'200','msg':list[r]}
    else:
        msg = {'STATUS':'200','msg':'WRONG DATA ELEMENT'}

    return jsonify(result=msg)

app.run(debug=True)