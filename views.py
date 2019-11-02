from flask import render_template, send_file, request

from . import util, app
from .forms import URLForm
from download import Convert


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    return render_template('index.html', form=form)


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    form = URLForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            links = form.urls.data.splitlines()
            for yturl in links:
                ytget = Convert(yturl, form.vid.data, form.bit.data)
                ytget.dl_convert()
            file, name = util.zip_files()
            return send_file(file, attachment_filename=name, as_attachment=True, mimetype='application/download')
    return render_template('index.html', form=form)


@app.route('/download', methods=['GET', 'POST'])
def download():
    print("Is this happening")
    if request.method == 'POST':
        file, name = util.zip_files()
        return send_file(file, attachment_filename=name, as_attachment=True)
    return 'Do nothing'
