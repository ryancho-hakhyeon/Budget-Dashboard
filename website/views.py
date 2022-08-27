from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# home page
@views.route('/')
@views.route('home')
def home_page():
    return render_template('home.html')


@views.route('/Analytics')
def analytics_page():
    return render_template('analytics.html')