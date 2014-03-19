#-*- coding: utf-8 -*-

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models
from forms import PostForm
from models import Story
from datetime import datetime
from config import STORIES_PER_PAGE

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
	stories = models.Story.query.order_by('timestamp desc').paginate(page, STORIES_PER_PAGE, False)
	return render_template("index.html", stories = stories)


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	form = PostForm()
	if form.validate_on_submit():
		post = Story(title = form.title.data,
			body = form.body.data,
			location = form.location.data,
			pseudonym = form.pseudonym.data,
			time = form.time.data,
			timestamp = datetime.utcnow())
		db.session.add(post)
		db.session.commit()
		#flash("Thank you, this site depends on people like you. Here's your story!")
		return redirect(url_for("story",
			id = str(post.id)))
	return render_template("submit.html",
		form = form)
		

@app.route('/story/<id>')
def story(id):
	story = models.Story.query.get(id)
	return render_template("story.html",
		story = story)

@app.route('/vote/<id>')
def vote(id):
	story = models.Story.query.get(id)
	if request.method == 'POST':
		vote = request.form['vote']
		if vote == 'up':
			voting = Vote(story_id = story.id, value = 1)
		else:
			voting = Vote(story_id = story.id, value = -1)
		
		db.session.add(voting)
		db.session.commit()
	
