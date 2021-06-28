import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


def xlsx_to_csv_pd():
    data_xls = pd.read_excel(r'C:\Users\milan\Documents\WeChat Files\sheng095296\FileStorage\File\2021-06\123456.XLS', index_col=0)
    data_xls.to_csv('123456.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()
    result = pd.read_csv(r'C:\Users\milan\Documents\WeChat Files\sheng095296\FileStorage\File\2021-06\123456.XLS')
    result.profile_report()