"""CSV Cleaner Upper"""
import pandas as pd

csv = pd.read_csv(
    "C:/Users/ggadbois/Documents/Personal Files/Projects/Albion/albiondata/Albion Online Database.csv")
df = pd.DataFrame(csv)



print(df)
