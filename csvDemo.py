import csv
#CSV stands for Comma-Separated Values. It stores tabular data in plain text where each row is a line and values are separated by commas (or another delimiter like ;).
#every row should be treated as list in csv
with open("utilities/loanAPP.csv") as csvFile:  #when nothing is return its default read file
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
    print(names)
    print(status)
    Index=names.index('Mohit')
    loanStatus = status[Index]
    print("Mohit's loanstatus is : " + loanStatus)

with open('utilities/loanAPP.csv' , 'a', newline='') as WFile:  #for write file we have to mention 'w' but this completely erase previous data in file so here we wrote 'a' means append the data
    # newline - Recommended by Python docs to avoid extra blank lines, especially on Windows
     write = csv.writer(WFile)
     write.writerow(["sweety" , "denied"])   #we have to write data in list format this method takes a list as input