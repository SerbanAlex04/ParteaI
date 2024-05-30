import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('../Date/cerinta5.csv')

nr_rows = len(df.axes[0])

male_titles = {}
female_titles = {}

for i in range(nr_rows):
    if df['Sex'][i] == 'male':
        if df['Name'].isna()[i] == 0:
            title = re.findall(", [^\.]*\.", df['Name'][i])
            title = title[0][2 :]
            try:
                male_titles[title] += 1
            except:
                male_titles[title] = 1
    if df['Sex'][i] == 'female':
        if df['Name'].isna()[i] == 0:
            title = re.findall(", [^\.]*\.", df['Name'][i])
            title = title[0][2 :]
            try:
                female_titles[title] += 1
            except:
                female_titles[title] = 1

print('Titluri de barbati:')

for key, value in male_titles.items():

    print(f'{key} : {value}')

print('Titluri de femei:')

print()

for key, value in female_titles.items():

    print(f'{key} : {value}')

plt.figure()
plt.title('male titles')
x = male_titles.keys()
y = male_titles.values()
plt.bar(x, y)
plt.xlabel('titlu')
plt.ylabel('numar aparitii')
plt.savefig('../output/cerinta9/male_titles')

plt.figure()
plt.title('female titles')
x = female_titles.keys()
y = female_titles.values()
plt.bar(x, y)
plt.xlabel('titlu')
plt.ylabel('numar aparitii')
plt.savefig('../output/cerinta9/female_titles')
