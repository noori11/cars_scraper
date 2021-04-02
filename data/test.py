import pandas as pd 
import requests
import os, time
import json

#Loading json data and datatransformation 
json_file = r'C:\Users\Admin\Documents\GitHub\cars\cars_scrap\cars_scrap\spiders\cars.json'

with open(json_file) as j: 
    data = json.load(j)

dataframe = pd.json_normalize(data, 'Aarsrapporter', meta=['CVR', 'Virksomhed'], errors='ignore')
PDF_data = dataframe[dataframe['Type'] == 'PDF'].groupby('CVR').first()
PDF_data ['CVR'] = PDF_data .index


#Getting a single pdf
for index, row in PDF_data[1:10].iterrows(): 
    cvr = row['CVR'] + '.pdf'  
    url = row['Link']
    path = os.path.join(os.getcwd(), cvr)

    #Downloding the file 
    r = requests.get(url, stream=True)

    with open(path, 'wb') as f:
        f.write(r.content)

    #Sending the file to cloud 
    files = {
        'file' : open(path, 'rb')
    }

    path = os.path.relpath(path, 'C:/Users/Admin/Documents/GitHub/cars/data/') 

    url = f"https://s3.eu-de.objectstorage.softlayer.net/cars-test-bucket/{path}"

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-amz-tagging': 'PDF',
    'Authorization': 'Bearer eyJraWQiOiIyMDIxMDMyMTE4MzUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjYwMDA3U0pXIiwiaWQiOiJJQk1pZC02NjYwMDA3U0pXIiwicmVhbG1pZCI6IklCTWlkIiwic2Vzc2lvbl9pZCI6IkMtOTQ4NzQyMGItYWU1My00NTI5LThlOGYtOWQxYWMzNjA5YWYzIiwianRpIjoiZWU3ZTY4ZDEtZTZhNy00YTJlLTg4ZmItOTk1ZDNiMzdiZDkwIiwiaWRlbnRpZmllciI6IjY2NjAwMDdTSlciLCJnaXZlbl9uYW1lIjoiUGFyd2V6IiwiZmFtaWx5X25hbWUiOiJOb29yaSIsIm5hbWUiOiJQYXJ3ZXogTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsInN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImF1dGhuIjp7InN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImlhbV9pZCI6IklCTWlkLTY2NjAwMDdTSlciLCJuYW1lIjoiUGFyd2V6IE5vb3JpIiwiZ2l2ZW5fbmFtZSI6IlBhcndleiIsImZhbWlseV9uYW1lIjoiTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJkNjRiNDU0OTczN2M0NjM2OGIxNjYyNDNhYWFhM2EyZiJ9LCJpYXQiOjE2MTczOTQ2MTAsImV4cCI6MTYxNzM5NTgxMCwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOnBhc3Njb2RlIiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiYngiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.f70htRepemXGwf3i20x4KWGv6WyXfIFsmDzudgoWELzaNKICEWOUgHOC1P3J3OV1Z4_9QrdrzMtpojXrwcYa0_kF6UlZv34wKc6jduQ5Jxcbi_WDNuaqDDZ6gh4sAmuZSTHtAdLir01Zn6iBYBN7jll94Yyit8_EOSTPJRGuQLSWghqhUnvpLwoMF0qtkSL7kTl9GLGVAmlSnwqSMuMoNsbHQfV6TSyOzzTojA-OlO2PUDoHlSRdxTpAXXP8pz3fqAfjCutV9TxiqIFNrAarQ-oylEzi1iCYRRC1g1ZWXVNIJGoobCdcKcjbHPChXZhrxF_P6VGWG9H74sjNQ-4MaA'
    }

    response = requests.request("PUT", url, headers=headers, files=files)
    print(response.status_code)




"""
Bucket 1 (PDF): 
1.cvr.pdf, tag=PDF  

Bucket 2 (XBRL): 
1. cvr_dato.xbrl, tag=xbrl

"""

