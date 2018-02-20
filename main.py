from flask import Flask, request, render_template
from input_checks import valid_email, valid_length, match

app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def process():
    username = request.form['username']
    password_1 = request.form['password']
    password_2 = request.form['verify']
    email = request.form['email']

    if valid_length(username):
        return render_template('welcome.html')
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run()