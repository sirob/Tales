#-*- coding: utf-8 -*-

from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models
from forms import PostForm
from models import Story
from datetime import datetime
from config import STORIES_PER_PAGE
from sqlalchemy import func

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page = 1):
	# stories = models.Story.query.order_by('votes desc').paginate(page, STORIES_PER_PAGE, False)
	start_index = (page) * STORIES_PER_PAGE
	results = db.session.query\
		(func.sum(models.Vote.value).label('votes'), models.Story).\
		join(models.Story).\
		group_by(models.Story.id).\
		order_by('votes desc').\
		offset(start_index)
	stories = [r[1] for r in results]
	
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

@app.route('/vote/<id>', methods=['POST'])
def vote(id):
	print "id: " + str(id)
	story = models.Story.query.get(id)
	if request.method == 'POST':
		ip_addr = request.remote_addr
		vote = request.form['vote']
		if vote == 'up':
			voting = models.Vote(story_id = story.id, value = 1, ip_addr = ip_addr)
		else:
			voting = models.Vote(story_id = story.id, value = -1, ip_addr = ip_addr)
		
		db.session.add(voting)
		db.session.commit()

		print 'count:' + str(story.vote_count())
	
		return str(story.vote_count())


@app.route('/vote/count')
def vote_count():
	count = len(models.Vote.query.all())
	return str(count)