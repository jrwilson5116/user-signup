from flask import Flask, request, render_template
import input_checks

app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('templates/index.html')



if __name__=="__main__":
    app.run()