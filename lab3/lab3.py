import csv

# variables
flights = []
terminals = []
start1, start2, finish1, finish2 = [], [], [], []
path = "C:/Users/Code/Python"
j = 0
k = 0
test = True
needNewTerminal = True

# reading all the times from excel csv files
file1 = open(path + "/finish1.CSV", "r")
reader1=csv.reader(file1)
for line in reader1:
    finish1.append(line[0])
file1.close()

file2 = open(path + "/start1.CSV", "r")
reader2=csv.reader(file2)
for line in reader2:
    start1.append(line[0])
file2.close()

file3 = open(path + "/finish2.CSV", "r")
reader3 = csv.reader(file3)
for line in reader3:
    finish2.append(line[0])
file3.close()

file4 = open(path + "/start2.CSV", "r")
reader4 = csv.reader(file4)
for line in reader4:
    start2.append(line[0])
file4.close()

# 2d list where each row has a start and finish time to make schedule
for x in range(0, len(start1)-1) :
    flights.append([start1[x],finish1[x]])

for i in range(1,len(start1)) :
    # creates the first terminal
    if i == 0 :
        terminals.append([flights[i][0], flights[i][1]])
    # runs every time after the first terminal is made
    else :
        k=0
        test = True
        needNewTerminal=True
        while(k<len(terminals)) :
            # this is done if flight fits in current terminal
            if float(flights[i-1][0]) >= float(terminals[k][-1]) :
                terminals[k].append(flights[i-1][0])
                terminals[k].append(flights[i-1][1])
                needNewTerminal=False
            else :
                k+=1
        # this is done if new terminal is needed for a flight
        if (needNewTerminal):
            terminals.append([flights[i][0], flights[i][1]])

print(terminals)
numOfTerminals = len(terminals)
print(f"For the given schedule, the minimum number of terminals required is {numOfTerminals:d}")