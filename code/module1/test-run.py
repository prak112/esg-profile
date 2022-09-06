#%%
# Trial approach with Camelot PDF library for extracting tables
# Possibility to convert tables to .csv or dataframe, instantly

#%%
# import libraries
from lib2to3.pgen2.token import RBRACE
import pandas as pd
import camelot
import csv

print("Libraries imported.")
#%%
# read dataset pdf
tables = camelot.read_pdf(r"D:\GitHub_Projects\esg-profile\dataset\global-top-100-companies-2021.pdf", pages="22")

#tables.export("test.csv", f="csv", compress=True)
print(tables)
tables[3].to_csv('test.csv')

# %%
# CSV to Dataframe
df = pd.read_csv('test.csv', skiprows=2, header=1, skipinitialspace=True)
df.head()
# %%
# CSV to Reader to parse \n within string --- NAILED IT!!!!!
# ----------------------------------------------------------
# Need to save the extracted items in a list...

with open ('test.csv') as f:
    reader = csv.reader(f, delimiter='\n')
    for row in reader:
        if str.find(row[0], '\n') != -1:
            items = str.split(row[0], '\n')
            print("Length of each row : ",len(items))
            if len(items) < 4:
                continue
            else:
                final_split = str.split(items[3], ',"')
                items = items[:3]
                for item in final_split:
                    items.append(item)
                print(items)
        else:
            continue

# %%

# %%
