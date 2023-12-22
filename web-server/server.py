from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

#url parameters

@app.route("/<username>/<int:post_id>")
def url_para(username=None, post_id=None):
    return render_template('index.html', name=username, id=post_id)

@app.route("/wazzup")
def wazzup():
    return "<p>Wazzzaaaaaap My Boyzz!!!!</p>"

@app.route("/about")
def about():
    return render_template('about.html')

