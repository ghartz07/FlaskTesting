import git
from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/skyshade/FlaskTesting')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/third_page")
def third_page():
    return render_template('third_page.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")