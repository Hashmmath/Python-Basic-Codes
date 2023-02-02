'''To scrape data from a website using Python, you can use the 
requests library to make a request to the website's server and 
retrieve the HTML content, and then use a library like beautifulsoup 
to parse the HTML and extract the desired data. 
Here's an example that scrapes the title of a webpage:'''

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("title").text
print("Title:", title)

'''This code makes a GET request to the specified URL using the requests.get() 
function and stores the response in the response variable. The response.content 
attribute contains the HTML content of the webpage, which is then passed to the 
BeautifulSoup constructor to create a soup object that can be used to parse the HTML. 
The soup.find() method is used to find the first <title> tag in the HTML and retrieve its text.'''
