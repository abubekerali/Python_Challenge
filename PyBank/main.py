import csv


   #import CSV files.
   csvpath = "budget_data_2.csv"
   resultsfile= "Financial_Analysis.txt"

   

with open(csvpath, newline="") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     #Empty Lists to store data.
   Total_No_months = []
   Total_Revenue = []
   Average_Revenue_Change = []
   Greatest_Revenue_Increase = []
   Greatest_Revenue_Decrease= []
        #total month
  for rows in csvreader: 
      numMonths= 0
        #Add months to counter
      numMonths += 1
        
        #The total number of months included in the dataset.
      total_months.append(numMonths)
        print(numMonths) 
    
        #The total amount of revenue gained over the entire period.
      revenue = sum(int(row[1]))
      total_revenue.append(revenue)
      print(revenue)       
    
      #The average change in revenue between months over the entire period
      average = revenue/numMonths
      average_revenue_change.append(average)
      print(average)

      #The greatest increase in revenue (date and amount) over the entire period
      revenue_list = []
      numRevenue = 0
      numRevenue += 1
       
      revenue_list.append(numRevenue)
      max(revenue_list)
      greatest_increase_revenue.append(max(revenue_list))
      print(max(revenue_list))       
      #The greatest decrease in revenue (date and amount) over the entire period
      min(revenue_list)   
      greatest_decrease_revenue.append(min(revenue_list))
      print(min(revenue_list))       
