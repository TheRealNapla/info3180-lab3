from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators= [DataRequired(), Length(min = 2, max = 100)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    subject = StringField('Subject', validators= [DataRequired()])
    message = TextAreaField('Message', validators= [DataRequired()])
    submit = SubmitField('Send')