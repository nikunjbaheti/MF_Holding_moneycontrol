import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import string

url = "https://www.moneycontrol.com/mutual-funds/uti-nifty-index-fund-direct-plan/portfolio-holdings/MUT657"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# Get Holdings Table
table=soup.find(id="equityCompleteHoldingTable")

#Headers
headers = [header.text for header in table.find_all('th')]

rows=[]

def cleanTableRecord(tableRecord):
     # cleanRecord=tableRecord.text.translate(None,string.whitespace)
     # cleanRecord=cleanRecord.text.translate('','-')
     to_remove = {'-','\n'}
     table = {ord(char): None for char in to_remove}
     cleanRecord = tableRecord.text.translate(table)
     cleanRecord=cleanRecord.strip()
     return cleanRecord


#Get All rows
for row in table.find_all('tr'):
     rows.append([cleanTableRecord(val)  for val in row.find_all('td')])

#Write
with open('csv/uti-nifty.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in rows)



