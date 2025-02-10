import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the financials page
url = 'https://www.marketwatch.com/investing/stock/tsla/financials?mod=mw_quote_tab'

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the financial data
table = soup.find('table', {'class': 'table'})

# Extract the headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract the rows
rows = []
for row in table.find_all('tr')[1:]:
    rows.append([cell.text.strip() for cell in row.find_all('td')])

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to an Excel sheet
df.to_excel('financials.xlsx', index=False)

print("Data has been saved to financials.xlsx")