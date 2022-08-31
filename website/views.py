from flask import Blueprint, render_template, request
from website.models import Dataset


views = Blueprint('views', __name__)


# home page
@views.route('/')
@views.route('home')
def home_page():
    return render_template('home.html', )


@views.route('/Analytics', methods=['POST', 'GET'])
def analytics_page():
    datasets = Dataset().get_data()
    new_date = datasets.loc[(datasets['year'] == 2022) & (datasets['month'] == 'Aug')]
    print(new_date)

    if request.method == 'POST':
        year = request.form.get('line_year')
        month = request.form.get('line_month')
        date = f'{year} {month}'
        dataset = {
            'title': date,
            'data': [12, 19, 3, 5, 2, -3],
            'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        }
        return render_template('analytics.html', dataset=dataset)
    else:
        dataset = {
            'title': 'AUGUST DETAIL',
            'data': [12, 19, 3, 5, 2, -3],
            'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        }
        return render_template('analytics.html', dataset=dataset)


@views.route('/Analytics-pie')
def analytics_pie():
    return render_template('detail-pie.html')


@views.route('/Total-table')
def total_page():
    return render_template('total-table.html')