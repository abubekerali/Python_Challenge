# importing the csv package
import csv
import re

filename= "D:\\Data_Science\\GW-DataAnalytics\\HomeWork\\Python\\Python_Challenge\\PyParagraph\\Paragraph_1.txt "
with open(filename,'r',) as textfile:
  textreader= csv_reader(textfile)
 # initiating list storage  
Approximate word count=[]
Approximate Sentence Count=[]
Average letter Count=[]
Average Sentence length=[]


for line in textreader:
  wordlist= line.split()
  Approximate word count= len(wordlist)
  
  sentencelist=re.split(r'[.!?]+', textreader)
  Approximate Setence count= len(sentencelist)

