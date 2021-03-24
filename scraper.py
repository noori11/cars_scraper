import os 
import requests 
from bs4 import BeautifulSoup
import time 

cvr_numre = [69749917]


# class OurScraper: 

#     def __init__(self):
#         """ Init our custom scraper """ 
    
#     def scrape_cvr(self, cvr):
    

url = "https://filingaccess.serff.com/sfa/home/insurancecompact"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') 
links = soup.find_all('a')
print("Total amount of links found:",len(links))


print(links)