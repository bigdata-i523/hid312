def make_reports():

    from acceleparser import dataparse
    from Tables import stepsBYweekday, stepsBYdate
    from Visualizations import stepsBYweekdayGraph, stepsBYdateGraph
    import matplotlib.pyplot as plt
    import glob

    files = glob.glob('iPhoneData/*.xml')

    counter = 1
    file = files[counter]
    for i in files:
        if counter <= len(files):


            df = dataparse(data= file)
            file_name = ("Client" + str(counter))

            graph1 = stepsBYdateGraph(df)
            plt.savefig(file_name + "StepsByDate.pdf")
            plt.close()
            graph2 = stepsBYweekdayGraph(df)
            plt.savefig(file_name+"StepsByDayOfWeek.pdf")
            plt.close()

            table1 = stepsBYweekday(df)

            f = open(file_name+".txt","w")
            f.write("Client " + str(counter) + " Report\n\n")
            f.write("Steps by Week\n")
            f.write(str(table1)+"\n\n")
            f.close()

            counter = counter + 1

make_reports()












