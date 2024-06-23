from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)
    else:
        return redirect(url_for('student'))

if __name__ == '__main__':
    app.run(debug=True)
