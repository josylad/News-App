from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
# from wtforms.validators import Required


class ReviewForm(FlaskForm):

    title = StringField('Review Title')
    review = TextAreaField('Movie Review')
    submit = SubmitField('Submit')