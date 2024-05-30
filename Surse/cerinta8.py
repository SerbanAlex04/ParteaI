import pandas as pd

df = pd.read_csv('../titanic/train.csv')

nr_rows = len(df.axes[0])

for col in df.axes[1]:

    null_values = df[col].isna().sum()

    if null_values > 0:

        if df[col].dtypes == int or df[col].dtypes == float:

            suma_alive = 0
            nr_alive = 0
            suma_not_alive = 0
            nr_not_alive = 0

            for i in range(nr_rows):
                if df[col].isna()[i] == 0:
                    if df['Survived'][i] == 1:
                        suma_alive += df[col][i]
                        nr_alive += 1
                    else:
                        suma_not_alive += df[col][i]
                        nr_not_alive += 1

            media_alive = suma_alive // nr_alive
            media_not_alive = suma_not_alive // nr_not_alive

            for i in range(nr_rows):
                if df[col].isna()[i] == 1:
                    if df['Survived'][i] == 1:
                        df.loc[i, col] = media_alive
                    else:
                        df.loc[i, col] = media_not_alive
        else:
            frecv_alive = {}
            frecv_not_alive = {}

            for i in range(nr_rows):
                if df[col].isna()[i] == 0:
                    if df['Survived'][i] == 1:
                        try:
                            frecv_alive[df.at[i, col]] += 1
                        except:
                            frecv_alive[df.at[i, col]] = 1
                    else:
                        try:
                            frecv_not_alive[df.at[i, col]] += 1
                        except:
                            frecv_not_alive[df.at[i, col]] = 1

            most_frequent_alive = max(frecv_alive.values())
            most_frequent_not_alive = max(frecv_not_alive.values())

            for key, value in frecv_alive.items():
                if value == most_frequent_alive:
                    most_frequent_alive_item = key
                    break

            for key, value in frecv_not_alive.items():
                if value == most_frequent_not_alive:
                    most_frequent_not_alive_item = key
                    break
            
            for i in range(nr_rows):
                if df[col].isna()[i] == 1:
                    if df['Survived'][i] == 1:
                        df.loc[i, col] = most_frequent_alive_item
                    else:
                        df.loc[i, col] = most_frequent_not_alive_item

df.to_csv('../Date/cerinta8.csv', index = 0)
