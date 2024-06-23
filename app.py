from flask import Flask
app=Flask(__name__)
@app.route('/')
def first_Pr():
    return "Run First Program"

if __name__=='__main__':
    app.run()