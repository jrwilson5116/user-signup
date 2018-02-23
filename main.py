from flask import Flask, request, render_template
from input_checks import valid_email, valid_length, match

app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('index.html').format("","","","")

@app.route("/",methods=['POST'])
def process():
    username = request.form['username']
    password_1 = request.form['password']
    password_2 = request.form['verify']
    email = request.form['email']

    msg_1 = ""
    msg_2 = ""
    msg_3 = ""
    msg_4 = ""

    if valid_length(username)and valid_length(password_1)and \
        match(password_1,password_2) and valid_email(email):
            return render_template('welcome.html').format(username)

    if not valid_length(username):
        msg_1 = "Invalid Username"
    if not valid_length(password_1):
        msg_2 = "Invalid Password"
    if not match(password_1,password_2):
        msg_3 = "Passwords do not match"
    if not valid_email(email):
        msg_4 = "Invalid Email"

    return render_template('index.html').format(msg_1,msg_2,msg_3,msg_4)

if __name__=="__main__":
    app.run()