import pandas as pd


class Dataset:

    def __int__(self):
        self.data = ''

    def get_data(self):
        self.data = pd.read_csv('dataset.csv')
        return self.data

    def set_data(self):
        pass