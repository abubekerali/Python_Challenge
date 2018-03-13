import csv


   #import CSV files.
Filepath = "D:\\Data_Science\\GW-DataAnalytics\\HomeWork\\Python\\Python_Challenge\\PyBank\\budget_data_2.csv"
   

   

with open(filepath, newline="") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     #Initiatng Lists .
   Months=0
   Total_No_months = []
   Total_Revenue = []
   Average_Revenue_Change = []
   Greatest_Revenue_Increase = []
   Greatest_Revenue_Decrease= []
        
  for rows in csvreader: 
      
        #Add months to counter
      Months += 1
        
        #The total number of months .
      Total_No_months.append(Months)
        
    
        #calculating the total revenue.
      revenue = sum(int(row[1]))
      Total_revenue.append(revenue)
            
    
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
