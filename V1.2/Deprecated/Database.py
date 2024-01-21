import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

PRICE_URL = r'https://west.albion-online-data.com/api/v2/stats/Prices/'

LOCATION = 'Caerleon'  # Set your desired location

class ProductSearchApp:
    def __init__(self, root, connection):
        self.root = root
        self.root.title("Product Search App")

        self.connection = connection

        self.create_widgets()

    def create_widgets(self):
        # ... (existing code)

        self.result_tree.bind("<ButtonRelease-1>", self.fetch_price_data)

    def search_product(self, event):
        # ... (existing code)

    def fetch_price_data(self, event):
        selected_item = self.result_tree.item(self.result_tree.selection())['values'][0]
        self.fetch_price(selected_item)

    def fetch_price(self, item_name):
        try:
            current_price_response = requests.get(PRICE_URL +
                                                  item_name +
                                                  'json?&locations=' +
                                                  LOCATION +
                                                  'Tiers',
                                                  timeout=10)

            if current_price_response.status_code == 200:
                market_prices = current_price_response.json()[0]['sell_price_min']
                print(f"Current price for {item_name}: {market_prices}")
            else:
                print(f"Error fetching price data. Status code: {current_price_response.status_code}")

        except requests.RequestException as e:
            print(f"Error during request: {e}")

# Example Usage
database_file_path = r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.2\calculator.db"
connection = connect_to_database(database_file_path)

if connection:
    root = tk.Tk()
    app = ProductSearchApp(root, connection)
    root.mainloop()

    # Close the connection when done
    close_connection(connection)
