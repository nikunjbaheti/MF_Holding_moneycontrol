import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd
import string

#Format for URL : http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/MBO225
def cleanTableRecord(tableRecord):
     # cleanRecord=tableRecord.text.translate(None,string.whitespace)
     # cleanRecord=cleanRecord.text.translate('','-')
     to_remove = {'-','\n'}
     table = {ord(char): None for char in to_remove}
     cleanRecord = tableRecord.text.translate(table)
     cleanRecord=cleanRecord.strip()
     return cleanRecord


def createCsvForRow(row):
    
    url = "http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/"+row['URL Tag']
    print(f'Plan :'+ row['URL Tag'] +' - URL :'+url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    table=soup.find(id="equityCompleteHoldingTable")
    if(table!=None):
        #Headers
        headers = [header.text for header in table.find_all('th')]
        rows=[]
        #Get All rows
        for holding in table.find_all('tr'):
             rows.append([cleanTableRecord(val)  for val in holding.find_all('td')])

        destinationPath='csv/'+row['URL Tag']+'.csv'
      #Write
        with open(destinationPath, 'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows)

df = pd.read_csv('csv/FundList.csv',delimiter=',')

for i, row in df[::-1].iterrows():
    createCsvForRow(row)

