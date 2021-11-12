log_file = open("um-server-01.txt") #opening the file


def sales_reports(log_file): #creates a function
    for line in log_file: #creating a for in loop to check if a certain line is "Tue"
        line = line.rstrip() #removes white space
        day = line[0:3] # tells which line or column the days are in
        if day == "Mon":
            print(line)# if it is then it prints the line


sales_reports(log_file)
