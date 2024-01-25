import pandas as pd
csv_df = pd.read_csv("../../parcours.csv", sep=';', index_col='date', parse_dates=True, dayfirst=True)
my_newindex = pd.date_range('2022-11-27', end='2023-03-25', freq='D')
csv_df_reindexed = csv_df.reindex(my_newindex, fill_value=0)
pd.set_option('display.max_rows',None)

all_datas = []

for index, row in csv_df_reindexed.iterrows():
    my_line = {}
    my_line['x'] = index.strftime('%Y-%m-%d')
    my_line['y'] = row['km']
    all_datas.append(my_line)


import json
with open('data.json', 'w') as fd:
    json.dump(all_datas, fd, indent=4)