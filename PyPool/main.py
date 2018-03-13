import csv
import os
file= "D:\\Data_Science\\GW-DataAnalytics\\HomeWork\\Python\\Python_Challenge\\PyPool\\election_data_1.csv"

with open(file,'r',newline="") as poolcsv:
    csvreader= csv.reader(poolcsv,delimiter=",")
    next(csvreader)

    
    for row in csvreader:
        Total_vote= len(row[0])
        print(Total_vote)
    
    