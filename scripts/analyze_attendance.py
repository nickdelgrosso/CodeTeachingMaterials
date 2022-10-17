# %%
from pathlib import Path
import pandas as pd


# %%
df = pd.concat(pd.read_csv(fname, index_col=0) for fname in Path('../data').glob('*.csv'))
df['meeting_date'] = pd.to_datetime(df['meeting_start_time']).dt.date
df.head()

# %%
names = {}
for _, row in df.iterrows():
    email = row['user_email']
    name = row['name']
    if email not in names or len(name) > len(row['user_email']):
        names[row['user_email']] = name
names


# %%
from pygments import highlight


total_minutes = (df.groupby(['meeting_topic', 'meeting_date', 'Participant Name', 'user_email'])[['duration']].sum() / 60 / 60) 
# total_minutes[total_minutes == False] = pd.NA
total_minutes
summary = total_minutes.reset_index()
summary
table = summary.pivot(index='user_email', columns='meeting_date', values='duration') > 4
table = table.reset_index()
table['user_name'] = [names[row['user_email']] for _, row in table.iterrows()]
cols = list(table.columns)
result = table[[cols[-1], cols[0]] + cols[1:-1]]
result




# %%
summary


