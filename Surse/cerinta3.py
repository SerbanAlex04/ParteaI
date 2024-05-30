import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../titanic/train.csv')

for col in df.axes[1]:
    if df[col].dtypes == int or df[col].dtypes == float:
        plt.figure()
        plt.title(col)
        plt.xlabel('values')
        plt.ylabel('frequencies')
        plt.hist(df[col])
        plt.savefig(f'../output/cerinta3/hist_{col}')
