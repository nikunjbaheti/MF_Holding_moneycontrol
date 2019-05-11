import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

url = "https://www.moneycontrol.com/mutual-funds/uti-nifty-index-fund-direct-plan/portfolio-holdings/MUT657"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

# Get Holdings Table
table=soup.find(id="equityCompleteHoldingTable")

#Headers
headers = [header.text for header in table.find_all('th')]

rows=[]
#Get All rows
for row in table.find_all('tr'):
     rows.append([val.text.encode('utf8')  for val in row.find_all('td')])

#Write
with open('csv/uti-nifty.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in rows if row)

