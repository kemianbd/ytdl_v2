from flask import render_template, send_file, request

from . import util, app
from .forms import URLForm, DLForm
from .download import Convert


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    dl_form = DLForm()
    if dl_form.validate_on_submit():
        file, name = util.zip_files()
        return send_file(file, attachment_filename=name, as_attachment=True, mimetype='audio/mpeg')
    return render_template('index.html', form=form, dl_form=dl_form)


@app.route('/convert', methods=['GET', 'POST'])
def convert():
    form = URLForm()
    dl_form = DLForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            links = form.urls.data.splitlines()
            ytget = Convert(form.vid.data, form.bit.data)
            for yturl in links:
                ytget.clear_files()
                ytget.dl_convert(yturl)
    return render_template('index.html', form=form, dl_form=dl_form)


@app.route('/pdf')
def pdf():
    return render_template('pdfcombine.html')
