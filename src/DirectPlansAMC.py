import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import string
import re


amc="TE"
#Trying out for Franklin - Getting equity 
url = "https://www.moneycontrol.com/mutual-funds/amc-details/"+amc
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# Get Holdings Table
allFundsForAMC=soup.findAll("a",attrs={'class':'arial11blue'})

mfRows=[]


for row in allFundsForAMC:
     mfRows.append([row.text,row.get('href').split('/')[-1]])


headers=["Fund Name","URL Tag"]
with open('csv/FundList.csv','w',newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in mfRows)

