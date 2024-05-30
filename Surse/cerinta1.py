import pandas as pd

df = pd.read_csv('../titanic/train.csv')

nr_col = len(df.axes[1])

types = df.dtypes

null_values = df.isna().sum()

nr_rows = len(df.axes[0])

if df.duplicated().sum() == 0:
    is_dup = 0
else:
    is_dup = 1

print(f"Numarul de coloane: {nr_col}\n")
print(f"Tiprile de date ale coloanelor:\n{types}\n")
print(f"Numarul de valori nule pe fiecare coloana:\n{null_values}\n")
print(f"Numarul de linii: {nr_rows}\n")
if is_dup == 0:
    print("Nu exista linii duplicate")
else:
    print("Exista linii duplicate")