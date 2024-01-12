"""Albion API Handler"""

import requests
import datetime
import pandas as pd
from openpyxl import load_workbook
import pathlib

PRICE_URL = "https://west.albion-online-data.com/api/v2/stats/prices/"
calc = pathlib.WindowsPath("C:/Users/gabri/Documents/Projects/Albion/AlbionCalculator v1.1.xlsx")

CALCULATOR = load_workbook(calc, data_only=True)
CALC = CALCULATOR["Calculator"]
calc_data = pd.ExcelFile("C:/Users/gabri/Documents/Projects/Albion/AlbionCalculator v1.1.xlsx")
calc_excel = pd.read_excel(calc_data, sheet_name="Items")
calc_df = pd.DataFrame(calc_excel)
LOCATION = CALC["A2"]

def parse_timestamp(timestamp):
    """Parses time stamps from API"""
    format_time = "%d-%m-%Y %H:%M"
    return datetime.datetime.strptime(timestamp, format_time)

def calc_inputs():
    """Returns the Excels items"""
    product     = CALC["B4"].value
    ingredient1 = CALC["B7"].value
    ingredient2 = CALC["B8"].value
    ingredient3 = CALC["B9"].value
    ingredient4 = CALC["B10"].value
    ingredient5 = CALC["B11"].value
    input_list = pd.DataFrame({"Item Name":
        [product, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5]})
    input_list = input_list[~(input_list == 0).all(axis=1)]
    return input_list

def calc_to_df():
    """Dataframe to Excel Comparison"""
    input_lists = calc_inputs()
    api_item = pd.merge(input_lists,calc_df, on="Item Name", how="left" )[["Item ID", "Item Name"]]
    return api_item

# REQUEST = requests.get(PRICE_URL + )



print(calc_to_df())
