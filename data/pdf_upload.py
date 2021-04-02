import pandas as pd 
import requests
import json

json_file = r'C:\Users\Admin\Documents\GitHub\cars\cars_scrap\cars_scrap\spiders\cars.json'

with open(json_file) as j: 
    data = json.load(j)

dataframe = pd.json_normalize(data, 'Aarsrapporter', meta=['CVR', 'Virksomhed'], errors='ignore')

#Selecting the file that will be downloaded for each of the file types 
iXBRL_data = dataframe[dataframe['Type'] == 'iXBRL' ].groupby('CVR').first()
XBRL_data = dataframe[dataframe['Type'] == 'XBRL'].groupby('CVR').first()
PDF_data = dataframe[dataframe['Type'] == 'PDF'].groupby('CVR').first()

#Adding CVR as a new column instead of indexes 
iXBRL_data['CVR'] = iXBRL_data.index


#Request
import urllib.request
urllib.request.urlretrieve(url, "filename.pdf")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


for index, row in iXBRL_data[1:10].iterrows(): 
  CVR = row['CVR']  
  url = row['Link']
  urllib.request.Request(url, r"{CVR}.pdf", headers = hdr)


#Uploading the material to the bucket in IBM Cloud object storage 

filename = '32324242'
_type = 'pdf'
url = f"https://s3.eu-de.objectstorage.softlayer.net/cars-test-bucket/{filename}.{_type}}"



payload = "This is another test data for the text fil3e."
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'x-amz-tagging': 'PDF',
  'Authorization': 'Bearer eyJraWQiOiIyMDIxMDMyMTE4MzUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjYwMDA3U0pXIiwiaWQiOiJJQk1pZC02NjYwMDA3U0pXIiwicmVhbG1pZCI6IklCTWlkIiwic2Vzc2lvbl9pZCI6IkMtOWI5ZjI0ZWMtNDUzNy00M2RjLTliMDktODkzNGVmYzUwYWM0IiwianRpIjoiNjhkYTJhMjEtZTkzNy00YTg3LTlkMTItZWVlODIzYTU0MGQwIiwiaWRlbnRpZmllciI6IjY2NjAwMDdTSlciLCJnaXZlbl9uYW1lIjoiUGFyd2V6IiwiZmFtaWx5X25hbWUiOiJOb29yaSIsIm5hbWUiOiJQYXJ3ZXogTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsInN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImF1dGhuIjp7InN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImlhbV9pZCI6IklCTWlkLTY2NjAwMDdTSlciLCJuYW1lIjoiUGFyd2V6IE5vb3JpIiwiZ2l2ZW5fbmFtZSI6IlBhcndleiIsImZhbWlseV9uYW1lIjoiTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJkNjRiNDU0OTczN2M0NjM2OGIxNjYyNDNhYWFhM2EyZiJ9LCJpYXQiOjE2MTcxODk2NDIsImV4cCI6MTYxNzE5MDg0MiwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOnBhc3Njb2RlIiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiYngiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.XFws38rv2VENta7bF4uWgReXmBdhhgkhwbNmkobYwxile4BDCwze-ozkx7ZZC80mTdwGxYf_15gkZT8t78UeiG0LJ-GM1knAEFG4mem8gL0_bgQ-W0H8l4qHk3xX-obI00DNbdXiC6aezrY_7DkvgTJnCqlOq2rKHQPD3j3ZV67LUhdU4ZSXwpCnn4nwNyF8uc056ru-KdBIwvkWu-giS0_Bx_66w8Jgweh4qFHfohe0nKeI3xVAgnIlScO4DGIgLZRLxETemGojgrNPSRi7unffue8Uz5GfyK8ySsjuJfTBSKWKMJ3utyZZgR_Nh9QKNXyYZmbgCySZb25trlWAZA'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)


"""
Bucket 1 (PDF): 
1.cvr.pdf, tag=PDF  

Bucket 2 (XBRL/XML): 
1. cvr_dato.XML, tag=xbrl

"""