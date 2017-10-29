#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
from datetime import datetime

testing = True

app = Flask('home-app', template_folder='templates')

cnt = 0

@app.route('/clock')
def get_clock_now():
    clock_now = datetime.strftime(datetime.now(), '%H : %M : %S')
    global cnt
    cnt += 1
    return jsonify(dict(clock=clock_now, counter=cnt))


@app.route('/')
def my_clock():
    return render_template('clock.html')

if __name__ == '__main__':

    if testing:
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0')
