'''This code assumes that the webpage contains a table with 
a class name of my-table, and that the table has three 
columns of data. You'll need to adjust the code accordingly 
for your specific use case.'''


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the webpage
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the data
table = soup.find('table', {'class': 'my-table'})

# Extract the data from the table and store it in a list of dictionaries
data = []
rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if cells:
        data.append({
            'Column 1': cells[0].text.strip(),
            'Column 2': cells[1].text.strip(),
            'Column 3': cells[2].text.strip(),
        })

# Create a Pandas dataframe from the list of dictionaries
df = pd.DataFrame(data)

# Save the dataframe to an Excel file
df.to_excel('mydata.xlsx', index=False)
