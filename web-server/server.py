from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

#url parameters

# @app.route("/<username>/<int:post_id>")
# def url_para(username=None, post_id=None):
#     return render_template('index.html', name=username, id=post_id)

@app.route("/")
# @app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    return 'Form submitted'

# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

