from app import db

class Story(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(140), unique = True)
	body = db.Column(db.Text(1400))
	location = db.Column(db.String(64))
	#timestamp = db.Column(db.DateTime)
	pseudonym = db.Column(db.String(64), unique = True)
	email = db.Column(db.String(120), unique = True)

	def __repr__(self):
		return '<Story %r>' % (self.title)