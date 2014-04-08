from app import db

class Story(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(90)) #75 sta dve polni vrstici
	body = db.Column(db.Text(1800))
	location = db.Column(db.String(64))
	time = db.Column(db.String(90))
	timestamp = db.Column(db.DateTime)
	pseudonym = db.Column(db.String(64))
	votes = db.Column(db.Integer)

	def __repr__(self):
		return '<Story %r>' % (self.title)

class Vote(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	story_id = db.Column(db.Integer, db.ForeignKey("story.id"))
	ip_addr = db.Column(db.Integer)
	value = db.Column(db.Integer)

	def __repr__(self):
		return '<Vote %r>' % (self.story_id)