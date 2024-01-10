"""Albion Online Web Scraper"""

from nbformat import convert
from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://albiononline2d.com/en/item/cat/accessories/subcat/bag"

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get(URL)
action = webdriver.ActionChains(driver)

item_categories = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div/div[4]')
for items in item_categories:
    elements = items.find_elements(By.CLASS_NAME, '"col-xl-4 col-lg-6 col-md-6"')

print(elements)