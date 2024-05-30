import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('../Date/cerinta5.csv')

nr_rows = len(df.axes[0])

nr_singles = 0
nr_singles_alive = 0
nr_not_singles = 0
nr_not_singles_alive = 0

for i in range(nr_rows):
    if (df['SibSp'][i] + df['Parch'][i]) == 0:
        nr_singles += 1
        if df['Survived'][i] == 1:
            nr_singles_alive += 1
    else:
        nr_not_singles += 1
        if df['Survived'][i] == 1:
            nr_not_singles_alive += 1

proc_single_survived = nr_singles_alive / nr_singles * 100
proc_not_single_survived = nr_not_singles_alive / nr_not_singles * 100

x = ['single on  board', 'not single on board']
y = [proc_single_survived, proc_not_single_survived]
plt.ylabel('procent survived')
plt.title('how being single on board influenced surviving')
plt.bar(x, y)
plt.savefig('../output/cerinta10/single_or_not')

plt.figure()
sb.catplot(data = df.head(100), x = 'Pclass', y = 'Fare', hue = 'Survived', kind = 'swarm', aspect = 3)

plt.savefig('../output/cerinta10/tarif_clasa')