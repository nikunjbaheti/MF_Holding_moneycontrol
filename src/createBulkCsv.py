import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Format for URL: http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/MBO225
def clean_table_record(table_record):
    to_remove = {'-', '\n'}
    table = {ord(char): None for char in to_remove}
    clean_record = table_record.text.translate(table)
    clean_record = clean_record.strip()
    return clean_record

def create_csv_for_row(row):
    url = "http://www.moneycontrol.com/india/mutualfunds/mfinfo/portfolio_holdings/" + row['URL Tag']
    print(f'Plan: {row["URL Tag"]} - URL: {url}')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find(id="equityCompleteHoldingTable")
    
    if table is not None:
        # Headers
        headers = [header.text for header in table.find_all('th')]
        rows = []
        # Get all rows
        for holding in table.find_all('tr'):
            rows.append([clean_table_record(val) for val in holding.find_all('td')])

        destination_path = f'csv/{row["URL Tag"]}.csv'
        # Write
        with open(destination_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(row for row in rows)

df = pd.read_csv('csv/FundList.csv', delimiter=',')

for i, row in df[::-1].iterrows():
    create_csv_for_row(row)
