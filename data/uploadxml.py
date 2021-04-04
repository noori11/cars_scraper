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
            'Authorization': 'Bearer _'
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


