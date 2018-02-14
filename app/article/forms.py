# Import packages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm):
	"""
	Form for article to add or edit
	"""
	title = StringField('Title',  validators=[DataRequired()])
	description = StringField('Description')
	submit = SubmitField('Submit')
	