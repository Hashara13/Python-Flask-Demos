from flask import Flask, request, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user=request.form('name')
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('UserID',user)
        return resp
    
@app.route('/getcookie')
def getcookie():
    if request.method == 'POST':
        name=request.cookies.get('UserID')
        return '<h1>welcome '+name+'<h1>'


if __name__ == '__main__':
    app.run(debug=True)
