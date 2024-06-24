from flask import Flask, request, session, abort, flash, redirect, url_for, render_template, make_response
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        f=request.files('file')
        f.save(secure_filename(f.filename))
        return 'upload done'

if __name__ == '__main__':
    app.run(debug=True)
