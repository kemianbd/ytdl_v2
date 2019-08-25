from flask import render_template

from . import main
from .forms import URLForm
from download import Convert


@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        links = form.urls.data.splitlines()
        for yturl in links:
            ytget = Convert(yturl, form.file.data, form.vid.data, form.bit.data)
            ytget.dl_convert()
    return render_template('index.html', form=form)
