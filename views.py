from flask import render_template, send_file

from . import main
from .forms import URLForm
from download import Convert


@main.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        links = form.urls.data.splitlines()
        for yturl in links:
            ytget = Convert(yturl, form.vid.data, form.bit.data)
            ytget.dl_convert()
        return send_file(ytget.zip_files(), attachment_filename='downloads.zip', as_attachment=True)
    return render_template('index.html', form=form)
