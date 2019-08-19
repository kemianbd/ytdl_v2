from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired


class URLForm(FlaskForm):
    urls = wtforms.TextAreaField('Enter YouTube URLs', validators=[DataRequired()])
    bit = wtforms.SelectField('Choose bitrate:',
                              choices=[('192k', '192k'), ('256k', '256k'), ('320k', '320k')], default='256k')
    vid = wtforms.BooleanField('Keep video?')
    file = wtforms.StringField('Save location', validators=[DataRequired()])
    run = wtforms.SubmitField('Run')
