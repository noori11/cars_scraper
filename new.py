import requests
from bs4 import BeautifulSoup
url = 'https://www.cookcountyassessor.com/Search/Property-Search.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
i = soup.find('input', {'class':'navbar'})
print(i['value'])