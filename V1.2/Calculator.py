import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime

def connect_to_database(database_file):
    """Access DB"""
    try:
        connection = sqlite3.connect(database_file)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def close_connection(connection):
    """Close DB"""
    if connection:
        connection.close()

def fetch_data_by_product(connection, product_name):
    """Pulls Data from DB"""
    query = "SELECT Product, Category_Name, Tiers FROM Calculator_Items WHERE Product LIKE ?"
    try:
        data = pd.read_sql_query(query, connection, params=('%' + product_name + '%',))
        return data
    except sqlite3.Error as e:
        print(f"Error fetching data: {e}")
        return None

class ProductSearchApp:
    """Containment of GUI"""
    def __init__(self, root, connection):
        self.root = root
        self.root.title("Crafting Calculator")
        self.connection = connection
        self.create_widgets()

    def create_widgets(self):
        """Main Frameowork of GUI"""
        self.search_label = tk.Label(self.root, text="Search Product:")
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.pack(pady=10)
        self.search_entry.bind("<KeyRelease>", self.search_product)

        self.result_tree = ttk.Treeview(self.root, columns=['Product'], show="headings")
        self.result_tree.heading('Product', text='Product')
        self.result_tree.pack(pady=10)
        self.result_tree.bind("<ButtonRelease-1>", self.select_item)

        self.fetch_button = tk.Button(self.root, text="Fetch Prices", command=self.fetch_prices)
        self.fetch_button.pack(pady=10)

    def search_product(self, event):
        """Search for Items within the GUI"""
        product_name = self.search_entry.get()
        data = fetch_data_by_product(self.connection, product_name)

        for item in self.result_tree.get_children():
            self.result_tree.delete(item)

        if data is not None:
            for index, row in data.iterrows():
                # Display only 'Product' in the GUI
                self.result_tree.insert("", "end", values=[row['Product']])

    def select_item(self, event):
        """Returns Items for GUI"""
        selected_item = self.result_tree.selection()
        if selected_item:
            selected_value = self.result_tree.item(selected_item, "values")[0]
            self.search_entry.delete(0, tk.END)
            self.search_entry.insert(0, selected_value)

    def fetch_prices(self):
        """Pulls the Prices from API"""
        selected_value = self.search_entry.get()
        
        # Get the current time and format it
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Add the current time to the API call
        api_url = f'https://west.albion-online-data.com/api/v2/stats/Prices/{selected_value}?time={current_time}'
        response = requests.get(api_url)

        if response.status_code == 200:
            prices_data = response.json()
            print(prices_data)
        else:
            print(f"Failed to fetch prices. Status code: {response.status_code}")

database_file_path = r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.2\calculator.db"
connection = connect_to_database(database_file_path)

if connection:
    root = tk.Tk()
    app = ProductSearchApp(root, connection)
    root.mainloop()

    close_connection(connection)
