class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all
                
    def show_report(self, df, title=None):
        if title:
            print(title)

        rows_count = df.shape[0]
        columns_count = df.shape[1]
        duplicates = df.duplicated().sum()

        # Вывод информации о датасете
        print('Количество столбцов:', columns_count)
        print('Количество строк:', rows_count)

        print('Количество дубликатов:', duplicates)

        print('Доля дубликатов:', format(duplicates / rows_count, self.percent_format))

        # Описательная статистика по числовым и категориальным столбцам:
        print(df.describe(include='all' if self.include_all else None))

        # Статистика по количеству пропущенных значений:
        print('Количество пропусков:', df.isna().sum().sum())
        print('Доля пропусков:',
                format(
                    df.isna().sum().sum() / (rows_count * columns_count),
                    self.float_format
                ))

import pandas as pd

data = pd.read_csv('data/payments.csv')


reporter_1 = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
reporter_2 = DataFrameReporter(float_format='0.03f', percent_format='0.01%', include_all=True)

reporter_1.show_report(data, 'Отчёт в формате 1:')
print()
reporter_2.show_report(data, 'Отчёт в формате 2:')