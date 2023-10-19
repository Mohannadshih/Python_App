from flask import Flask, Blueprint, render_template
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('test.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')