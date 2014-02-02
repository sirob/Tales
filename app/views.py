from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
from forms import PostForm
from models import Story
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
	story1 = {'title': 'Najbl nora storija evah'} #fake storie titles
	story2 = {'title': 'Mal mn nora storija'}
	story3 = {'title': 'Cist mal nora storija'}
	story4 = {'title': 'Neki neki'}
	story5 = {'title': 'Neki'}
	story6 = {'title': 'Se neki'}
	return render_template("index.html",
		story1 = story1,
		story2 = story2,
		story3 = story3,
		story4 = story4,
		story5 = story5,
		story6 = story6,
		)

@app.route('/submit_story', methods = ['GET', 'POST'])
def submit_story():
	form = PostForm()
	if form.validate_on_submit():
		post = Story(title = form.post.data)
		db.session.add(post)
		db.session.commit()
		flash('Your story has been published!')
		return redirect(url_for("story.html"))
	return render_template("submit_story.html",
		form = form)
		

@app.route('/story/<title>')
def story():
	return render_template("story.html",
		title = title)