from flask import Flask, Blueprint, render_template
import requests

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/listing')
def listing():
    return render_template('list.html')

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
