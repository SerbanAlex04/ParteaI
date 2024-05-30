import pandas as pd

df = pd.read_csv('../titanic/train.csv')

nr_rows = len(df.axes[0])

for col in df.axes[1]:
    nr_nulls = df[col].isna().sum()
    if nr_nulls != 0:
        print(f'Valori lipsa pentru coloana {col}: {nr_nulls}')
        proportion = nr_nulls / nr_rows
        print(f'Proportia de valori lipsa in coloana {col}: {proportion * 100 :.2f}%')
        nr_survived = 0
        nr_not_survived = 0
        nr_nulls_survived = 0
        nr_nulls_not_survived = 0
        for i in range(nr_rows):
            if df.at[i, 'Survived'] == 1:
                nr_survived += 1
                if df[col].isna()[i] == 1:
                    nr_nulls_survived += 1
            else:
                nr_not_survived += 1
                if df[col].isna()[i] == 1:
                    nr_nulls_not_survived += 1
        print(f'Procentul de valori lipsa in coloana {col}, pe Survived = 1: {nr_nulls_survived / nr_survived * 100 :.2f}%')
        print(f'Procentul de valori lipsa in coloana {col}, pe Survived = 0: {nr_nulls_not_survived / nr_not_survived * 100 :.2f}%')
        print()
