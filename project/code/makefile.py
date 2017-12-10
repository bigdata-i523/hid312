# creates reports and graphs of client steps for each iPhone data file
def make_reports():

    # imports user defined functions and necessary packages
    from acceleparser import dataparse
    from Tables import stepsBYweekday, corr_steps_weekday
    from Visualizations import stepsBYweekdayGraph, stepsBYdateGraph, stdv_stepsBYweekdayGraph, corr_graph
    import matplotlib.pyplot as plt
    import glob

    # defines xml file to read for each iteration
    files = glob.glob('iPhoneData/*.xml')
    files.reverse()
    counter = 0




    # iterates table and graph functions over each xml file and writes
    # output to txt and pdf files
    for i in files:

        if counter <= len(files):
            file = files[counter]
            df = dataparse(data= file)
            file_name = ("Client" + str(counter+1))

            # saves plots as pdf for each iteration
            graph1 = stepsBYdateGraph(df)
            plt.savefig(file_name + "StepsByDate.pdf")
            plt.close()
            graph2 = stepsBYweekdayGraph(df)
            plt.savefig(file_name+"MeanStepsByDayOfWeek.pdf")
            plt.close()
            graph3 = stdv_stepsBYweekdayGraph(df)
            plt.savefig(file_name + "StDevStepsByDayOfWeek.pdf")
            plt.close()
            graph4 = corr_graph(df)
            plt.savefig(file_name + "ScatterplotOfStepsByDayOfWeek.pdf")
            plt.close()
            # saves table as txt for each iteration
            table1 = stepsBYweekday(df)
            table2 = corr_steps_weekday(df)
            f = open(file_name+".txt","w")
            f.write(file_name + " Report\n\n")
            f.write("Steps by Week\n")
            f.write(str(table1)+"\n\n")
            f.write("Correlation of Steps with Day of the Week\n")
            f.write(str(table2)+"\n\n")
            f.close()

            counter = counter + 1

make_reports()

















