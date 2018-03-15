import csv


#import CSV files.
filepath = "D:\\Data_Science\\GW-DataAnalytics\\HomeWork\\Python\\Python_Challenge\\PyBank\\budget_data_2.csv"
   

with open(filepath, newline="") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

  #Initiatng Lists .
     Months=[]
     Total_No_months = []
     Total_Revenue = []
     Average_Revenue_Change = []
     Greatest_Revenue_Increase = []
     Greatest_Revenue_Decrease= []
        
for row in csvreader: 
      
      #Add months to counter
      Months += 1
        
      #The total number of months .
      Total_No_months.append(Months)
        
    
      #calculating the total revenue.
      revenue = sum(int(row[1]))
      Total_revenue.append(revenue)
            
    
      #To calculate the average revenue change looping through current and previous month
for i in range (len(csvreader)-1):
       #getting the current revenue
       current= csvreader[i+1]
       current_revenue= int(current[1])
       # getting the previous revenue
       previous=csvreader[i]
       previous_revenue= int(previous[1])
       #Computing the revenue change on monthly basis
       revenue_change= (current_revenue-previous_revenue)
       #computing the Average revenue
       Average_Revenue_Change.append(revenue_change/Total_No_months)
       
      #The greatest increase in revenue 
for i in range(len(csvreader)-1):
        if (csvreader[i+1][1]-csvreader[i])==max(revenue_change):
          Greatest_Revenue_Increase= max(revenue_change)
          Greatest_revenue_increase_month= csvreader[i+1][0]
      #The greatest decrease in revenue 
        elif (csvreader[i+1][1]-csvreader[i])==min(revenue_change):
          Greatest_Revenue_Decrease= min(revenue_change)
          Greatest_revenue_increase_month= csvreader[i+1][0]

with open("Financial_Analysis.txt", "w") as text_file:
    text_file.write("Total months: %s" % Total_No_months)
    text_file.write("Total Revenue: %s" % Total_Revenue )
    text_file.write("Average Revenue Change: %s" % Average_Revenue_Change )
    text_file.write("Greatest increase in revenue: %s" % Greatest_revenue_increase_month )
    text_file.write("Greatest Decrease in revenue: %s" % Greatest_revenue_Decrease_month )