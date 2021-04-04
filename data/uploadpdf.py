"""
Bucket: 
1.cvr.pdf, tag=PDF  

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
PDF_data = dataframe[dataframe['Type'] == 'PDF'].groupby('CVR').first()
PDF_data ['CVR'] = PDF_data .index
PDF_data.reset_index(drop=True, inplace=True)


def uploadfiles():
    try:
        for index, row in PDF_data[3922:len(PDF_data.index)].iterrows(): 
            print(f'{index} out of {len(PDF_data.index)}')
            cvr = row['CVR'] + '.pdf'  
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
            'x-amz-tagging': 'Type=pdf',
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



