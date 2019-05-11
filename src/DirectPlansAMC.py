import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import string
import re

#Format for URL : http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/MBO225

amc="TE"
#Trying out for Franklin - Getting equity 
url = "https://www.moneycontrol.com/mutual-funds/amc-details/"+amc
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# Get Holdings Table
allFundsForAMC=soup.findAll("a",attrs={'class':'arial11blue'})

mfRows=[]


for row in allFundsForAMC:
     mfRows.append([row.get('href').split('/')[-1]+","+row.text])


headers=["Fund Name","URL Tag"]
with open('csv/FundList.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in mfRows)

