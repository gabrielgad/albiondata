"""CSV Cleaner Upper"""
import io
import pandas as pd
import requests
import re

EVIL_STRINGS = r"^(?!.*https:\/\/albiononline2d).*$"
GOOD_STRINGS = r"(https:\/\/albiononline2d)"

URL = "https://raw.githubusercontent.com/gabrielgad/albiondata/Main/Albion%20Online%20Database.csv"
req = requests.get(URL, timeout=10).content
csv = pd.read_csv(io.StringIO(req.decode('utf-8')))

DF = pd.DataFrame(csv)
DF1 = DF['Title'].replace(r'[\d,"]+', '', regex=True)
DF1 = DF1.to_frame()
DF['Title'] = DF1['Title']
DF = DF.drop(DF.columns[[3,4,5,6,7,8,9,10,11,16,18,19,20,21,22,23,24,25,26,27]], axis=1)
DF.columns = ['Product', 'Product_URL', 'Product_Image', 'Ingredient', 
              'Ingredient_URL', 'Ingredient_Image', 'Ingredient_Name', 
              'Ingredient_Amount']

DF[['Ingredient', 'Ingredient_Name']] = DF[['Ingredient_Name', 'Ingredient']]
DF = DF.drop(columns=['Ingredient_Name'])

Mismatched = DF[DF['Product_URL'].str.contains(EVIL_STRINGS, regex=True, na=False)]
# Mismatched.to_excel('Mismatched.xlsx', sheet_name="Sheet1", index=False)

CorrectDF = DF[DF['Product_URL'].str.contains(GOOD_STRINGS, regex=True, na=False)]
CorrectDF.to_excel('CorrectedDF.xlsx', sheet_name="Sheet1", index=False)
print(DF)
