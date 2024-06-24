from flask import Flask, request, session, abort, flash, redirect, url_for, render_template, make_response
from flask_mail import Mail, Message
from app.forms import ContactForm
app = Flask(__name__)
app.secret_key='development key'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   form=ContactForm()
   if request.method=='POST':
      if form.validate()==False:
         flash("Fill all fields")
         return render_template('contact.html',form=form)
      else:
         return render_template('success.html')
   if request.method=='GET':
      return render_template('contact.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
