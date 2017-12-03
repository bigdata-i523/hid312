# function that takes iPhone xml file and converts to pandas dataframe

def dataparse(data):

# import packages

    import xml.etree.ElementTree as ET
    import pandas as pd

# import and parse xml file

    tree = ET.parse(data)
    root = tree.getroot()

# create lists to construct into dataframe
    steps = []
    dtime = []

    x = 2           # sets new record to iterate over

# iterates over records, adding date/time and steps data
# to lists above
    for i in root :

        test = root[x].tag

        if test == 'Record':

            record = root[x].attrib
            if record['unit'] == 'count':
                steps.append(record['value'])
                dtime.append(record['endDate'])
                x = x + 1

#creates dataframe from lists
    df = pd.DataFrame(
        {'date/time': dtime,
         'steps': steps})
    df['steps'] = pd.to_numeric(df['steps'])
    df['date/time'] = pd.to_datetime(df['date/time'])
    return(df)







