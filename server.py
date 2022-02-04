from flask import Flask, render_template, send_from_directory, redirect
from flask import request
import os
import csv

app = Flask(__name__)


def checkFile(data_dic):
    with open("database.txt", "a") as fi:
        email = data_dic['email']
        subject = data_dic['subject']
        message = data_dic['message']
        fi.write(f'{email},{subject},{message};')


def checkCsv(data_dic):
    with open("database.csv", "a", newline='') as dbse:
        email = data_dic['email']
        subject = data_dic['subject']
        message = data_dic['message']
        csv_writer = csv.writer(dbse, delimiter=",",
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
def myHome():
    return render_template('index.html')


@app.route("/<string:user_web>")
def myWeb(user_web):
    return render_template(user_web)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            checkCsv(data)
            return redirect('thanky.html')
        except:
            return 'Error!, Not saved to Database'
    else:
        return 'Failed!'
