def stepsBYdate (df):
    import pandas as pd
    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    pvt_stepsBYdate = pd.pivot_table(df, index = ['date/time'],values= ['steps'],aggfunc= [sum])
    return(pvt_stepsBYdate)

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

    df_stepsBYweekday = pd.DataFrame.from_dict(
        {'Mon': MonSteps,
         'Tue': TueSteps,
         'Wed': WedSteps,
         'Thu': ThuSteps,
         'Fri': FriSteps,
         'Sat': SatSteps,
         'Sun': SunSteps},
        orient= 'index')
    df_stepsBYweekday_trans = df_stepsBYweekday.transpose()

    return(df_stepsBYweekday_trans)

