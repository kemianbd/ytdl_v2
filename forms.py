from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired


class URLForm(FlaskForm):
    urls = wtforms.TextAreaField('Enter YouTube URLs', validators=[DataRequired()])
    bit = wtforms.SelectField('Choose bitrate:', coerce=int,
                              choices=[(192, '192kb'), (256, '256kb'), (320, '320kb')], default=256)
    vid = wtforms.BooleanField('Keep video?')
    file = wtforms.StringField('Save location', validators=[DataRequired()])
    run = wtforms.SubmitField('Run')
