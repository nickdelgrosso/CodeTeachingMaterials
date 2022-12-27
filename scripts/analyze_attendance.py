# %%
from pathlib import Path
import pandas as pd 
from utils.time import overlapping_duration


# %%
df = pd.concat(pd.read_csv(fname, index_col=0) for fname in Path('./data').glob('*.csv'))
df = df.assign(join_time = pd.to_datetime(df['join_time']), leave_time = pd.to_datetime(df['leave_time']))
df.head()

# %%
participants = (
    df
    .assign(meeting_date = pd.to_datetime(df['meeting_start_time']).dt.date)
    .query('status != "in_waiting_room"')
    .rename(columns={'user_email': 'email'})
    .sort_values('join_time')
    .groupby(
        ['meeting_topic', 'meeting_date', 'email'], 
        # as_index = False,
    )
)

full = pd.DataFrame()
full['Name'] = participants.name.agg(lambda names: names.tolist()[-1])
full['Attendance'] = participants.apply(
    lambda group: overlapping_duration(group['join_time'].values, group['leave_time'].values),
    # lambda group: group['duration'].sum() / 60 / 60,
)


table = (
    full
    .reset_index()
    .pivot(
        index=['Name', 'email'], 
        columns='meeting_date', 
        values='Attendance',
    )
    .transform(lambda a: round(a.dt.seconds / 60 / 60, 1))
)

writer = pd.ExcelWriter(f'../attendance_{table.columns[0]}.xlsx')
table.to_excel(writer, sheet_name='Attendance')
table

# %%
success = table > table.median().mean() / 2
success.to_excel(writer, sheet_name='Credit')
success

# %%
writer.close()



# %%
