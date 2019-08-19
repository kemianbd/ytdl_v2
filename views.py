from flask import render_template

from . import main
from .forms import URLForm
from download import dl_convert


@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        dl_convert(form.urls.data, form.file.data, form.vid.data, form.bit.data)
        print(form.urls.data)
    return render_template('index.html', form=form)
