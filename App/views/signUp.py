from flask import Blueprint, render_template, request,flash,url_for,redirect
from flask_jwt import jwt_required

from App.controllers import(
    create_user,
    create_form
)

from App.models import SignUp

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods = ['GET'])
def init_signup():
  contentData = SignUp()
  return render_template('/signup.html',test = test)

