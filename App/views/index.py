from flask import Blueprint, redirect, render_template, request, send_from_directory

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/login')
def login_page():
    return render_template('login.html')


@index_views.route('/conduct', methods=['GET'])
def conduct_page():
    return render_template('conduct.html')
