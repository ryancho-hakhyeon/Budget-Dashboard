import pandas as pd


class Dataset:
    def __int__(self, year, month):
        self.year = year
        self.month = month

    def get_total_data(self):
        data = pd.read_csv('../dataset.csv')
        # df = data['year'].unique()

        income_each_year = data.groupby('year')['income'].sum()
        outcome_each_year = data.groupby('year')['outcome'].sum()

        income_year_month = data.groupby(['year', 'month'])['income'].sum()
        outcome_year_month = data.groupby(['year', 'month'])['outcome'].sum()

        return outcome_year_month

    def get_filter_data(self):
        data = pd.read_csv('../dataset.csv')

        return data

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month


temp = Dataset()


print(temp.get_total_data())