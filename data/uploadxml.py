"""
Bucket: 
1.cvr.xml, tag=XML  

This file uploads all pdf files from the json file onto IBM Cloud Object storage. 
It uploads into the pucket 

"""
import pandas as pd 
import requests
import os, time
import json

#Loading json data and datatransformation 
json_file = r'C:\Users\Admin\Documents\GitHub\cars\cars_scrap\cars_scrap\spiders\cars.json'

with open(json_file) as j: 
    data = json.load(j)

dataframe = pd.json_normalize(data, 'Aarsrapporter', meta=['CVR', 'Virksomhed'], errors='ignore')
XBRL_data = dataframe[dataframe['Type'] == 'XBRL'].groupby('CVR').first()
XBRL_data['CVR'] = XBRL_data.index
XBRL_data.reset_index(drop=True, inplace=True)

def uploadfiles():
    try: 
        for index, row in XBRL_data[2920:len(XBRL_data.index)].iterrows(): 
            print(f'{index} out of {len(XBRL_data.index)}')
            cvr = row['CVR'] + '.xml'  
            url = row['Link']
            path = os.path.join(os.getcwd(), cvr)

            #Downloding the file 
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)

            #Sending the file to cloud 
            files = {
                'file' : open(path, 'rb')
            }

            relative_path = os.path.relpath(path, 'C:/Users/Admin/Documents/GitHub/cars/data/') 
            url = f"https://s3.eu-de.objectstorage.softlayer.net/cars-data/{relative_path}"
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-amz-tagging': "Type=xml",
            'Authorization': 'Bearer eyJraWQiOiIyMDIxMDMyMTE4MzUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjYwMDA3U0pXIiwiaWQiOiJJQk1pZC02NjYwMDA3U0pXIiwicmVhbG1pZCI6IklCTWlkIiwic2Vzc2lvbl9pZCI6IkMtZWQ3OWQxM2MtMjUwNC00MzljLThlMjgtZWY0NTg5YjBhZTE4IiwianRpIjoiMTEwZGM4NTQtZjQyYi00NDE3LWIxNjItNGE1M2NiMTQyNmMxIiwiaWRlbnRpZmllciI6IjY2NjAwMDdTSlciLCJnaXZlbl9uYW1lIjoiUGFyd2V6IiwiZmFtaWx5X25hbWUiOiJOb29yaSIsIm5hbWUiOiJQYXJ3ZXogTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsInN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImF1dGhuIjp7InN1YiI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSIsImlhbV9pZCI6IklCTWlkLTY2NjAwMDdTSlciLCJuYW1lIjoiUGFyd2V6IE5vb3JpIiwiZ2l2ZW5fbmFtZSI6IlBhcndleiIsImZhbWlseV9uYW1lIjoiTm9vcmkiLCJlbWFpbCI6IlBhcndlei5Ob29yaS1DSUNAaWJtLmNvbSJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJkNjRiNDU0OTczN2M0NjM2OGIxNjYyNDNhYWFhM2EyZiJ9LCJpYXQiOjE2MTc0ODQzMzAsImV4cCI6MTYxNzQ4NTUzMCwiaXNzIjoiaHR0cHM6Ly9pYW0uY2xvdWQuaWJtLmNvbS9pZGVudGl0eSIsImdyYW50X3R5cGUiOiJ1cm46aWJtOnBhcmFtczpvYXV0aDpncmFudC10eXBlOnBhc3Njb2RlIiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiYngiLCJhY3IiOjEsImFtciI6WyJwd2QiXX0.cGFnHN5dFewtQ0IYUWJWoaABDm2x76Th52M1Pjz3EWzHDjsB-cIl2gYh3QmUewq5CAAkcYdBJBYboqwEwxpq8b-1Enlk0WE_8hJox8NDx5QtI4ocB5aKpJE99RZfvX2NbTDxWjWrG8XKrifjDEonajOPEHnnIQUdeWG6yFjzidCepwfJsZxy3hBgTK3PL8P9028GUu4W2pg4vQL_7-xfoZR93KaIqzl1HXE3zWMjTDnpUoYckuiAvjFZpbZXuyLawbYtmsDbDexR8HqlggLBASwQoWhWYHIhSriycxklrRPNHX-8kEDLkVxfTI0LxnTSLXV6PnFbSQtL1vd1VXBA7g'
            }
            response = requests.request("PUT", url, headers=headers, files=files)
            files['file'].close()
            code = response.status_code
            os.remove(path)

            if code == 403:
                print("The Bearer token needs to be renewed")
                break  

    except HTTPError as e:
        if e.status_code == 403:
            sys.exit(1)


uploadfiles()


