# Creates line graph of client steps by date
def stepsBYdateGraph(df):
    from Tables import stepsBYdate
    import matplotlib.pyplot as plt

    table1= stepsBYdate(df)
    Graph = table1.plot()
    plt.title('Client Steps By Date')
    return(Graph)

# Creates bar graph of mean of steps for each day of the week
def stepsBYweekdayGraph (df):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # formats date/time column to display only date and adds weekday column
    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    df['weekday'] = df['date/time'].dt.dayofweek

    # creates pivot table with rows of date and weekday and column of sum of steps
    pvt_stepsBYweekday = pd.pivot_table(df, index= ['date/time','weekday'], values= ['steps'], aggfunc= [sum])

    # selects step sums for each weekday and converts to a list
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

    # creates list of means of steps for each weekday
    Means = [np.mean(MonSteps),np.mean(TueSteps), np.mean(WedSteps), np.mean(ThuSteps), np.mean(FriSteps), np.mean(SatSteps), np.mean(SunSteps)]

    # creates lists for graph x axis
    DayNum = [0,1,2,3,4,5,6]
    Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # creates graph
    DaysGraph = plt.bar(x= DayNum, height= Means, label = 'Step by Day of the Week')
    plt.xticks(DayNum, Days)
    plt.title('Mean of Steps By Day of the Week')
    return (DaysGraph)


# Creates bar graph of standard dev. of steps for each day of the week

def stdv_stepsBYweekdayGraph(df):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # formats date/time column to display only date and adds weekday column
    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    df['weekday'] = df['date/time'].dt.dayofweek

    # creates pivot table with rows of date and weekday and column of sum of steps
    pvt_stepsBYweekday = pd.pivot_table(df, index=['date/time', 'weekday'], values=['steps'], aggfunc=[sum])

    # selects step sums for each weekday and converts to a list
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

    # creates list of standard dev. of steps for each weekday
    Means = [np.mean(MonSteps), np.mean(TueSteps), np.mean(WedSteps), np.mean(ThuSteps), np.mean(FriSteps),
             np.mean(SatSteps), np.mean(SunSteps)]
    StDv = [np.std(MonSteps), np.std(TueSteps), np.std(WedSteps), np.std(ThuSteps), np.std(FriSteps), np.std(SatSteps),
            np.std(SunSteps)]

    # creates lists for graph x axis
    DayNum = [0, 1, 2, 3, 4, 5, 6]
    Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # creates graph

    StDvGraph = plt.bar(x=DayNum, height=StDv, label='Step by Day of the Week')
    plt.xticks(DayNum, Days)
    plt.title('Standard Deviation of Steps By Day of the Week')

    return (StDvGraph)

def corr_graph(df):
    import pandas as pd
    # select only date from date/time column and add day of the week column
    df['date/time'] = pd.to_datetime(df['date/time'].dt.date)
    df['weekday'] = df['date/time'].dt.dayofweek

    # create dataframe with date, weekday, and daily total steps
    df = df.groupby(['date/time', 'weekday'], as_index=False).sum()
    graph = df.plot(y = 'steps', x = 'weekday', kind= 'scatter')
    return(graph)
