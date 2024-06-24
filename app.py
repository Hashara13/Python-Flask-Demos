from flask import Flask, request, session, abort, flash, redirect, url_for, render_template, make_response
from flask_mail import Mail, Message
app = Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='sender mail'
app.config['MAIL_PASSWORD']='sender mail password'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')
def index():
   msg=Message('Hello',sender='your mail',recipients=['sender mail'])
   msg.body="Flask Mail sender Activated"
   mail.send(msg)
   return 'Send !'

if __name__ == '__main__':
    app.run(debug=True)
