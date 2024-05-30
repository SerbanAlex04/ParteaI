import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Date/cerinta5.csv')

nr_rows = len(df.axes[0])

nr_survivors = {0 : 0, 1 : 0, 2 : 0, 3 : 0}

survivors_ages = []
known_age_men = 0

for i in range(nr_rows):
    if df['Sex'][i] == 'male':
        if df['Survived'][i] == 1:
            if df['AgeInterval'][i] != -1:
                nr_survivors[df['AgeInterval'][i]] += 1
                known_age_men += 1

for key, value in nr_survivors.items():
    print(f'Numarul de barbati din categoria de varsta {key} care au supravietuit : {value}')

for key in nr_survivors.keys():
    nr_survivors[key] = nr_survivors[key] / known_age_men * 100

plt.title('Procentul de supravietuire in functie de intervalul de varsta')
x = ['[0, 20]', '[21,40]', '[41,60]', '60+']
y = nr_survivors.values()
plt.xlabel('interval de varsta')
plt.ylabel('procent de supravietuitori')
plt.bar(x, y)
plt.savefig('../output/cerinta6/ages_survived')
