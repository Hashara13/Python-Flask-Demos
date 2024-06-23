from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return f"Hello welcome: {name}"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['Username']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('Username')
        return redirect(url_for('welcome', name=user))

if __name__ == '__main__':
    app.run(debug=True)
