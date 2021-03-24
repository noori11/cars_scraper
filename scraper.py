import os 
import requests 
from bs4 import BeautifulSoup
import time 



# class OurScraper: 

#     def __init__(self):
#         """ Init our custom scraper """ 
    
#     def scrape_cvr(self, cvr):
    

cvr_numre = 69749917


url = "https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id={cvr_numre}&soeg={cvr_numre}&language=da"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') 

mydivs = soup.find_all("div", {"class": "cvrreg"})
# links = soup.find_all('a')
print(mydivs)
print("Total amount of links found:",len(mydivs))

# link_list = []

# for link in links:
#     if ('.pdf' in link.get('href')):
#         filelink = link.get('href')

# print(filelink)

# response = requests.get(filelink) 

# open('test.pdf', 'wb').write(response.content)
