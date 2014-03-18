from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, Length, Email
from wtforms.ext.sqlalchemy.validators import Unique
from models import Story
import datetime

class PostForm(Form):
	title = TextField('title', validators = [Required(), Length(min = 1, max = 90)])
	body = TextAreaField('body', validators = [Required(), Length(min = 300, max = 1800)])
	location = TextField('location', validators = [Length(min = 2, max = 64)])
	timestamp = datetime.datetime.utcnow()
	pseudonym = TextField('pseudonym', validators = [Required(), Length(min = 1, max = 64)])
	time = TextField('time', validators = [Required(), Length(min = 1, max = 90)])