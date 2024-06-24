from flask import Flask, request,session,abort, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST': 
        if request.form['username']=='admin':
            return redirect(url_for('succes'))
        else:
            abort(401) # if username not admin
    else:
        return redirect(url_for('index'))
    
@app.route('/succes')
def succes():
    return 'login success'


if __name__ == '__main__':
    app.run(debug=True)
