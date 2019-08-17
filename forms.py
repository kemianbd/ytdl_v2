from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired


class URLForm(FlaskForm):
    urls = wtforms.TextAreaField('Enter YouTube URLs', validators=[DataRequired()])
    vid = wtforms.BooleanField('Keep video?')
    file = wtforms.StringField('Save location', validators=[DataRequired()])
    run = wtforms.SubmitField('Run')
