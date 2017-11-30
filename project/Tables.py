def stepsBYdate (df):
    import pandas as pd
    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    grouped = df.groupby(['date/time']).sum()
    return(grouped)

def stepsBYweekday (df):
    import pandas as pd

    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    df['weekday'] = df['date/time'].dt.dayofweek
    pvt_stepsBYweekday = pd.pivot_table(df, index= ['date/time','weekday'], values= ['steps'], aggfunc= [sum])
    Mon = pvt_stepsBYweekday.query('weekday == [0]')
    Tue = pvt_stepsBYweekday.query('weekday == [1]')
    Wed = pvt_stepsBYweekday.query('weekday == [2]')
    Thu = pvt_stepsBYweekday.query('weekday == [3]')
    Fri = pvt_stepsBYweekday.query('weekday == [4]')
    Sat = pvt_stepsBYweekday.query('weekday == [5]')
    Sun = pvt_stepsBYweekday.query('weekday == [6]')

    MonSteps = pd.Series.tolist(Mon['sum'])
    TueSteps = pd.Series.tolist(Tue['sum'])
    WedSteps = pd.Series.tolist(Wed['sum'])
    ThuSteps = pd.Series.tolist(Thu['sum'])
    FriSteps = pd.Series.tolist(Fri['sum'])
    SatSteps = pd.Series.tolist(Sat['sum'])
    SunSteps = pd.Series.tolist(Sun['sum'])

    df_stepsBYweekday = pd.DataFrame(
         [MonSteps,
         TueSteps,
         WedSteps,
         ThuSteps,
         FriSteps,
         SatSteps,
         SunSteps]
    )
    df_stepsBYweekday_trans = df_stepsBYweekday.transpose()
    df_stepsBYweekday_trans.columns = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    PreWeeks = df[['date/time','weekday']]
    Weeks = PreWeeks[PreWeeks['weekday'] == 0]
    UniqueWeeks = Weeks.drop_duplicates()
    UniqueWeeks = UniqueWeeks.rename(columns={'date/time': 'Week Of'})
    df_stepsBYweekday_trans_weeks = df_stepsBYweekday_trans.set_index(UniqueWeeks['Week Of'])

    return(df_stepsBYweekday_trans_weeks)


