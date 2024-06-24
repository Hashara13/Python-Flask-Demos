from flask import Flask, request, session, abort, flash, redirect, url_for, render_template, make_response

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def home():
    return render_template('flash.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password'
        else:
            flash('Login successful')
            flash('Logout here')
            return redirect(url_for('home'))
    return render_template('signin.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
