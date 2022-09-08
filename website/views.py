from flask import Blueprint, render_template, request
import datetime

from website.models import Dataset


views = Blueprint('views', __name__)


# home page
@views.route('/', methods=['GET'])
@views.route('Home', methods=['GET'])
def home_page():
    chart_datasets = dict()
    datasets = Dataset()

    income, outcome, total = datasets.get_total_data()
    total_income = sum(income.values())
    total_outcome = round(sum(outcome.values()), 2)
    current_balance = total_income - total_outcome

    chart_datasets = {
        'title': 'Total Income & Outcome',
        'income_each_year': {
            'bg_color': 'rgb(2, 117, 216)',
            'data': list(income.values()),
            'label': list(income.keys())
        },
        'total_income': '{:,.2f}'.format(total_income),
        'outcome_each_year': {
            'bg_color': 'rgb(240, 173, 78)',
            'data': list(outcome.values()),
            'label': list(outcome.keys())
        },
        'total_outcome': '{:,.2f}'.format(total_outcome),
        'current_balance': '{:,.2f}'.format(current_balance),
        'total_each_month': total
    }
    return render_template('home.html', dataset=chart_datasets)


@views.route('/Analytics', methods=['POST', 'GET'])
def analytics_page():
    datasets = Dataset()

    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def reformat_data(select_year, select_month):
        datasets.set_year(int(select_year))
        datasets.set_month(select_month)
        new_data = datasets.get_filter_data()

        # Reforms data
        _income = new_data['income'].tolist()
        _outcome = new_data['outcome'].tolist()
        _balance = [round(elem, 2) for elem in new_data['balance'].tolist()]
        _labels = new_data['date'].tolist()

        return _income, _outcome, _balance, _labels

    if request.method == 'POST':
        year = request.form.get('line_year')
        month = request.form.get('line_month')

        # setting year and month into Dataset
        income, outcome, balance, labels = reformat_data(year, month)

        date = f'{month}. {year}'
        chart_datasets = {
            'title': date,
            'data': {'income': income, 'outcome': outcome, 'balance': balance},
            'labels': labels
        }
        return render_template('analytics.html', dataset=chart_datasets)
    else:
        year = today.year
        month = months[int(today.month)-1]
        date = f'{month}. {year}'

        income, outcome, balance, labels = reformat_data(year, month)

        chart_datasets = {
            'title': date,
            'data': {'income': income, 'outcome': outcome, 'balance': balance},
            'labels': labels
        }

        return render_template('analytics.html', dataset=chart_datasets)


@views.route('/Analytics-pie', methods=['GET', 'POST'])
def analytics_pie():
    datasets = Dataset()

    chart_datasets = {
        'title': 'AUGUST DETAIL',
        'data': [12, 19, 3, 5, 2, -3],
        'labels': ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        'temp': [{'te': 222}, {'te': 111}]
    }

    return render_template('detail-pie.html', dataset=chart_datasets)


@views.route('/Total-table', methods=['GET'])
def total_page():
    datasets = Dataset()
    data = datasets.get_table_data()

    return render_template('total-table.html', dataset=data)