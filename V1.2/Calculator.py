import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk
import requests  # Import the requests library for API calls

def connect_to_database(database_file):
    """Initial call on DB for reference"""
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def close_connection(connection):
    """Exit call on SQL Query"""
    if connection:
        connection.close()

def fetch_data_by_product(connection, product_name):
    """Fetches Values to call on API"""
    query = "SELECT Product FROM Calculator_Items WHERE Product LIKE ?"
    try:
        data = pd.read_sql_query(query, connection, params=('%' + product_name + '%',))
        return data
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return None

class ProductSearchApp:
    """Main App Container"""
    def __init__(self, root, connection):
        self.root = root
        self.root.title("Product Search App")

        self.connection = connection

        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self.root, text="Search Product:")
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.pack(pady=10)
        self.search_entry.bind("<KeyRelease>", self.search_product)

        self.result_tree = ttk.Treeview(self.root, columns=['Product'], show="headings")
        self.result_tree.heading('Product', text='Product')
        self.result_tree.pack(pady=10)

        # Button to fetch prices
        self.fetch_button = tk.Button(self.root, text="Fetch Prices", command=self.fetch_prices)
        self.fetch_button.pack(pady=10)

    def search_product(self, event):
        product_name = self.search_entry.get()
        data = fetch_data_by_product(self.connection, product_name)

        # Clear previous results
        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        if data is not None:
            for index, row in data.iterrows():
                self.result_tree.insert("", "end", values=[row['Product']])

    def fetch_prices(self):
        product_name = self.search_entry.get()
        # You may need to replace 'your_api_key' with a valid API key if required by the API
        api_url = f'https://west.albion-online-data.com/api/v2/stats/Prices/{product_name}'
        response = requests.get(api_url)

        if response.status_code == 200:
            prices_data = response.json()
            # Process and display prices_data as needed
            print(prices_data)
        else:
            print(f"Failed to fetch prices. Status code: {response.status_code}")

# Used Call
database_file_path = r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.2\calculator.db"
connection = connect_to_database(database_file_path)

if connection:
    root = tk.Tk()
    app = ProductSearchApp(root, connection)
    root.mainloop()

    # Close the connection when done
    close_connection(connection)
