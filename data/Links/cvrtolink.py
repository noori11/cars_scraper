"""
This script converts a list of cvr numbers to a list of cvr links, which can 
be accessed directly through an http request. Reformats the scrings to 
an actual representation of the links that shows the webpage of the company under
virk.cvr.dk 
"""

import pandas as pd  
import csv

df = pd.read_csv(r"cvr.csv")
mys = 'https://datacvr.virk.dk/data/visenhed?enhedstype=virksomhed&id=&type=undefined&language=da&q=visenhed/'

new_list=[]
nested=[]
for i, row in df.itertuples(): 
    new_list.append(f"{mys[:63]}{row}{mys[63:]}")

nested.append(new_list)

file = open("new_cvr.csv", 'a') 
writer = csv.writer(file, dialect='excel', lineterminator='\n')

for link in nested:
    writer.writerows([link])

file.close()
