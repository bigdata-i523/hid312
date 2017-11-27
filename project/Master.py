def make_reports():

    from acceleparser import dataparse
    from Tables import stepsBYweekday, stepsBYdate
    import glob

    files = glob.glob('iPhoneData/*.xml')

    counter = 1
    file = files[counter]
    for i in files:
        if counter <= len(files):


            df = dataparse(data= file)

            table1 = stepsBYdate(df)
            table2 = stepsBYweekday(df)

            txt_file_name = ("Client" + str(counter))
            f = open(txt_file_name+".txt","w")
            f.write("Client " + str(counter) + " Report\n\n")
            f.write("Steps by Day of the Week\n")
            f.write(str(table2))
            f.close()

            counter = counter + 1

make_reports()





