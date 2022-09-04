import pandas as pd


class Dataset:
    import pandas as pd
    def __int__(self, year, month):
        self.year = year
        self.month = month

    def get_total_data(self):
        data = pd.read_csv('./dataset.csv')
        # df = data['year'].unique()

        income_each_year = data.groupby('year')['income'].sum().to_dict()
        outcome_each_year = data.groupby('year')['outcome'].sum().to_dict()

        total_year_month = data.groupby(['year', 'month'], sort=False).agg(
                total_income=('income', 'sum'),
                total_outcome=('outcome', 'sum')
            ).reset_index().to_dict(orient='records')

        # The same result
        # total_year_month = data.groupby(['year', 'month']).agg({'income':'sum', 'outcome':'sum' })
        # total_year_month = data.groupby(['year', 'month'])[['income', 'outcome']].sum()

        return income_each_year, outcome_each_year, total_year_month

    def get_filter_data(self):
        data = pd.read_csv('./dataset.csv')

        filtered_data = data.loc[(data['year'] == self.year) & (data['month'] == self.month)]
        return filtered_data

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month


# temp = Dataset()
#
# # get total
# income, outcome, total = temp.get_total_data()
#
# print(list(outcome.values()))

# temp.set_year(2022)
# temp.set_month('Jul')
# temp.get_filter_data()['date'].values.tolist()
# print(temp.get_filter_data())
