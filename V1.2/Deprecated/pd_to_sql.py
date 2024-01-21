
import sqlite3
import pandas as pd

CSV_DB = r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.2\FinalizedDB.csv"

Final_DB = pd.read_csv(CSV_DB)
Final_DB.drop(columns=['Unnamed: 0'], inplace=True)

# Ensure 'Product' column is defined before using it
Final_DB['Product'] = Final_DB['Product'].astype(str)

# Extract the tier number from the Category_Name column
Final_DB['Tier'] = Final_DB['Category_Name'].str.extract(r'_LEVEL(\d+)', expand=False).astype(str)
Final_DB['New_Tier'] = Final_DB['Category_Name'].str.extract(r'@(\d+)', expand=False).astype(str)

Final_DB['Tiers'] = Final_DB['Tier'] + Final_DB['New_Tier']
Final_DB['Tiers'] = Final_DB['Tiers'].str.extract(r'(\d+)')
Final_DB.drop(['Tier', 'New_Tier'], axis=1, inplace=True)
Final_DB['Product'] = Final_DB['Product'] + Final_DB['Tiers'].fillna('')
Final_DB.to_csv('FinalizedDB1.1.csv')

# Create or connect to an SQLite database
conn = sqlite3.connect('calculator.db')

# Use the to_sql method to write the DataFrame to an SQLite table
Final_DB.to_sql('Calculator_Items', conn, index=False, if_exists='replace')

# Close the connection
conn.close()
