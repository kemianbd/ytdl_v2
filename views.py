from flask import render_template

from . import main
from .forms import URLForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        print(form.urls.data)
        print(form.vid.data)
    return render_template('index.html', form=form)
