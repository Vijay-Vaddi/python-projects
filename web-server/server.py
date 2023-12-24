from flask import Flask, render_template, request, redirect
import csv

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
        dataBase.write(f"\n{email},{subject},{message}")

def save_to_csv(data):
    with open('web-server/database.csv', mode='a', newline='',) as dataBase2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(dataBase2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return 'Something went wrong. Try again please.'
    else: 
        return 'something went wong'

