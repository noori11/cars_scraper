import pandas as pd 
import requests
import json

json_file = r'C:\Users\Admin\Documents\GitHub\cars\cars_scrap\cars_scrap\spiders\cars.json'

with open(json_file) as j: 
    data = json.load(j)

dataframe = pd.json_normalize(data, 'Aarsrapporter', meta=['CVR', 'Virksomhed'], errors='ignore')



print(dataframe)