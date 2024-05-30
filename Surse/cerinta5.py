import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../titanic/train.csv')

nr_rows = len(df.axes[0])
nr_cols = len(df.axes[1])

nr_intervals = {0 : 0, 1 : 0, 2 : 0, 3 : 0}

age_index = 0

for i in range(nr_cols):
    if df.axes[1][i] == 'Age':
        age_index = i
        break

df.insert(int(age_index + 1), 'AgeInterval', -1)

for i in range(nr_rows):
    if df['Age'][i] >= 0 and df['Age'][i] <= 20:
        nr_intervals[0] += 1
        df.loc[i, 'AgeInterval'] = 0
    if df['Age'][i] >= 21 and df['Age'][i] <= 40:
        nr_intervals[1] += 1
        df.loc[i, 'AgeInterval'] = 1
    if df['Age'][i] >= 41 and df['Age'][i] <= 60:
        nr_intervals[2] += 1
        df.loc[i, 'AgeInterval'] = 2
    if df['Age'][i] >= 61:
        nr_intervals[3] += 1
        df.loc[i, 'AgeInterval'] = 3

nr_ages = 0

for key, value in nr_intervals.items():
    nr_ages += value
    print(f'Numarul de pasageri din intervalul {key} : {value}')

print(f'Numarul de pasageri pentru care nu cunoastem varsa: {nr_rows - nr_ages}')

df.to_csv('../Date/cerinta5.csv', index = 0)

plt.hist(df['AgeInterval'])
plt.savefig('../output/cerinta5/ages')
