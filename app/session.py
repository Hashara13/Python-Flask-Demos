from flask import Flask, request,session, redirect, url_for, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"{username} is logged in from here <br><a href='/logout'>Logout</a>"
    return "You are not logged in <br><a href='/login'>Click here to login</a>"

@app.route('/login', methods=['GET', 'POST'])
def setcookie():
    if request.method == 'POST':
        session['username']=request.form('username')
        return redirect(url_for('index'))
    return render_template('session.html')
    
@app.route('/logout')
def getcookie():
    session.pop('username',None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
