import csv
import datetime
filepath= "D:\Data_Science\GW-DataAnalytics\HomeWork\Python\Python_Challenge\PyBoss\employee_data1.csv"

with open(filepath,newline="") as file:
    reader = csv.reader(file,delimiter=",")
    
    Formated_Employee_Data=[]
    Employee_Id=[]
    First_Name=[]
    last_Name=[]
    DOB_Old=[]
    DOB=[]
    SSN=[]
    State=[]
    
    us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA','Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV','Wisconsin': 'WI','Wyoming': 'WY',}
    for row in reader:
        print(row[1])
        Employee_Id.append(row[0]) 

        Full_Name= row[1].split()

        
        First_Name.append(Full_Name[0:])
        last_Name.append(Full_Name[1:])
        
        DOB_Old=datetime.datetime.strptime(row[2],'%Y-%m-%d')
        DOB.append(DOB_Old)

        FullSSN= [row[3].split("-")]
        SSN.append(FullSSN[-1])
        

        
        if row[4]==us_state_abbrev.keys():
            State= us_state_abbrev.values()
        #Merging all the columns
        Formated_Employee_Data.append([Employee_Id,First_Name,last_Name, DOB,SSN,State])
        print(Formated_Employee_Data)
        #with open(Formated_Employee_Data,'w',newline="")

