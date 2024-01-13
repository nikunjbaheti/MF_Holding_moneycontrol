import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.moneycontrol.com/mutual-funds/uti-nifty-index-fund-direct-plan/portfolio-holdings/MUT657"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get Holdings Table
table = soup.find(id="equityCompleteHoldingTable")

# Headers
headers = [header.text for header in table.find_all('th')]

rows = []

def clean_table_record(table_record):
    to_remove = {'-', '\n'}
    table = {ord(char): None for char in to_remove}
    clean_record = table_record.text.translate(table)
    clean_record = clean_record.strip()
    return clean_record

# Get All rows
for row in table.find_all('tr'):
    rows.append([clean_table_record(val) for val in row.find_all('td')])

# Write
with open('csv/uti-nifty.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in rows)
