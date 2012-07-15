from fivehundred import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import sys
from fetchphotos import *

#create our application! :) 
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent = True)
# allow environment variable called FLASKR SETTINGS, 
# not complain if no such env key is set

@app.route("/")
def home():
    # return ""
    return render_template("base.html")
@app.route("/city")
def city_first():
    name = request.args.get('first')
    next = request.args.get('second')
    last = request.args.get('third')
    return do_city(name, next, last)
@app.route("/city/<name>")
def city(name):
    next = request.args.get('next')
    last = request.args.get('last')    
    return do_city(name, next, last)
    
def do_city(name, next, last):
    pl = getpx(name)
    sfw = sfw_screen(pl)
    top_list = top_px(sfw,25)
    top_name = top_url(top_list)
    fe = front_end_output(top_name,pl)    
    return render_template("city.html", json_data=fe, city=name, next=next, last=last)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
