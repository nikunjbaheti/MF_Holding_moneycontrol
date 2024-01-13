import requests
from bs4 import BeautifulSoup
import csv

mainURL = "https://www.moneycontrol.com/mutualfundindia/"
response = requests.get(mainURL)
soup = BeautifulSoup(response.text, "lxml")
mfRows = []

# Get AMC links
amcClass = soup.find_all(attrs={'class': 'amclink'})
for div in amcClass:
    links = div.find_all('a')

for amc in links:
    # Trying out for Franklin - Getting equity
    url = amc.get('href')
    print("Adding for" + url)
    response = requests.get(url)
    soupAmc = BeautifulSoup(response.text, "html.parser")

    allFundsForAMC = soupAmc.find_all("a", attrs={'class': 'arial11blue'})
    for row in allFundsForAMC:
        mfRows.append([row.text, row.get('href').split('/')[-1]])

headers = ["Fund Name", "URL Tag"]
with open('csv/FundList.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(row for row in mfRows)
