from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

def save_to_file(data):
    with open('web-server/database.txt', mode='a') as dataBase:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = dataBase.write(f'{email} {subject} {message}')
        

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_file(data)
        return redirect("/thank_you.html")
    else: 
        return 'something went wong'

