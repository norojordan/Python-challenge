 #First import the modules
import os
import csv


csvpath = os.path.join("../","Resources", "election_data.csv")


# Read the csv module
with open(csvpath) as csvfile:

    # CSV reader specifies comma delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(len(csvreader))
    print(csvreader)