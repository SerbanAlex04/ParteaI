import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../Date/cerinta5.csv')

nr_rows = len(df.axes[0])

nr_children = 0
nr_adults = 0

for i in range(nr_rows):
    if df['Age'][i] >= 0 and df['Age'][i] < 18:
        nr_children += 1
    if df['Age'][i] >= 18:
        nr_adults += 1

known_age_people = nr_children + nr_adults

proc_children = nr_children / known_age_people * 100
proc_adults = nr_adults / known_age_people * 100

print(f'Procentul de copii de la bord : {proc_children :.2f}%')

x = ['copii', 'adulti']
y = [proc_children, proc_adults]
plt.title('rata de supravietuire pentru copii si adulti')
plt.ylabel('procent de supravietuire')
plt.bar(x, y)
plt.savefig('../output/cerinta7/children_adults_survived')
