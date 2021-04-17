from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class formulario_link_video(FlaskForm):
    link_video = StringField('link_video', validators=[DataRequired()])