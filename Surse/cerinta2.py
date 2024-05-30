import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../titanic/train.csv')

nr_rows = len(df.axes[0])

nr_survived = 0
nr_not_survived = 0

for i in range(nr_rows):
    if df.at[i, 'Survived'] == 1:
        nr_survived += 1
    else:
        nr_not_survived += 1

survived_proc = nr_survived / nr_rows * 100
not_survived_proc = nr_not_survived / nr_rows * 100

print(f"Procentul persoanelor care au supravietuit: {survived_proc :.2f}%")
print(f"Procentul persoanelor care nu au supravietuit: {not_survived_proc :.2f}%")

print()

x = ['survived', 'not survived']
y = [survived_proc, not_survived_proc]

plt.bar(x, y)
plt.ylabel('procent')
plt.savefig('../output/cerinta2/survived_graph')

classes = {}

for i in range(nr_rows):
    try:
        classes[df.at[i, 'Pclass']] += 1
    except:
        classes[df.at[i, 'Pclass']] = 1

for key, value in classes.items():
    print(f"Procentul de persoane in clasa {key} : {value / nr_rows * 100 :.2f}%")

print()

x = [str(key) for key in classes.keys()]
y = [value / nr_rows * 100 for value in classes.values()]

plt.figure()
plt.bar(x, y)
plt.ylabel('procent')
plt.savefig('../output/cerinta2/classes_graph')

nr_male = 0
nr_female = 0

for i in range(nr_rows):
    if df.at[i, 'Sex'] == 'male':
        nr_male += 1
    else:
        nr_female += 1

male_proc = nr_male / nr_rows * 100
female_proc = nr_female / nr_rows * 100

print(f"Procentul barbatilor: {male_proc :.2f}%")
print(f"Procentul femeilor: {female_proc :.2f}%")

x = ['male', 'female']
y = [male_proc, female_proc]

plt.figure()
plt.bar(x, y)
plt.ylabel('procent')
plt.savefig('../output/cerinta2/gender_graph')
