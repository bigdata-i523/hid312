def stepsBYdateGraph(df):
    from Tables import stepsBYdate


    table1= stepsBYdate(df)
    table1.reset_index(inplace=True)
    table1.set_index('date/time').plot()
    return (table1)

def stepsBYweekdayGraph (df):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

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

    Means = [np.mean(MonSteps),np.mean(TueSteps), np.mean(WedSteps), np.mean(ThuSteps), np.mean(FriSteps), np.mean(SatSteps), np.mean(SunSteps)]
    DayNum = [0,1,2,3,4,5,6]
    Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    DaysGraph = plt.bar(x= DayNum, height= Means, label = 'Step by Day of the Week')
    plt.xticks(DayNum, Days)

    return (DaysGraph)

