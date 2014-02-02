from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class PostForm(Form):
	post = TextField('post', validators = [Required()])