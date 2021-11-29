#opens file
log_file = open("um-server-01.txt")

#creates a fuction that has a parament of the file opened
def sales_reports(log_file):
    #starts a for loop that runs so long as there is a line in the file
    for line in log_file:
        #sets line equal to line minus \n
        line = line.rstrip()
        #sets day equal to 3 characters starting at index 0
        day = line[0:3]
        #checks to see if the day is tuesday
        if day == "Mon":
            #print the line if the day is tuesday
            print(line)

#call the function to run
sales_reports(log_file)
