from flask import Blueprint, render_template
import csv

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/listing')
def listing():
    data = []
    with open('static/CSV/test1.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    return render_template('list.html', data=data)

@main.route('/data')
def data_page():
    return render_template('data.html')

@main.route('/api_test')
def api_page():
    return render_template('api_test.html')

@main.route('/form')
def form():
    return render_template('form.html')

@main.route('/log')
def login_page():
    return render_template('login.html')

@main.route('/misc')
def misc():
    return render_template('index.html')

@main.route('/simon')
def simon():
    return render_template('simon.html')
