# importing the csv package
import csv
import re

#filename= "D:\\Data_Science\\GW-DataAnalytics\\HomeWork\\Python\\Python_Challenge\\PyParagraph\\Paragraph_1.txt "
#Approximate word count=0
#Approximate Sentence Count=0
#Average letter Count=0
#Average Sentence length

filename= "abebe beso bela? where is it? i dont know the place. it depends on the street names. the next!"
#with open(filename,'r',) as textfile:
   # textreader= csv_reader(te)
     #for line in textfile:
         #wordlist= line.split()
         #Approximate word count= len(wordlist)
re.split(r'[.!?]+', filename)

