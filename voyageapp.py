from flask import redirect, url_for, render_template, request
from model import app, Task
import model

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("home.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
    return render_template("make_task.html")

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