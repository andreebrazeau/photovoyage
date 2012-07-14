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
    return render_template("home.html")

@app.route("/city/<name>")
def city(name):
    pl = getpx(name)
    sfw = sfw_screen(pl)
    top_list = top_px(sfw,25)
    top_name = top_url(top_list)
    fe = front_end_output(top_name,pl)

    next = request.args.get('next')
    last = request.args.get('last')
    return render_template("city.html", json_data=fe, city=name, next=next, last=last)



# @app.route("/add", methods=["POST"])
# def save_task():
# 	task = request.form['task']
# 	notes = request.form['notes']
# 	t = Task(task,notes)
# 	model.add(t)
# 	model.save_all()
# 	return render_template("success.html", task=task, notes=notes)

# @app.route("/edit<task_id>", methods = ["GET"])
# def edit_task(task_id):
# 	task = Task.query.get(task_id)
# 	return render_template("edit.html", title = task.title, notes = task.notes)

# @app.route("/edit<task_id>", methods = ["POST"])
# def save_edited_task(task_id):
# 	new_task = request.form['task']
# 	new_notes = request.form['notes']
# 	t = model.Task.query.get(task_id)
# 	t.title = new_task
# 	t.notes = new_notes
# 	model.save_all()
# 	print Task.query.get_all()
# 	return render_template("success.html", new_task = new_task)


if __name__ == "__main__":
	app.run(debug=True)