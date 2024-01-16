"""This is the final 1.1 DF for sql usage later"""

import pandas as pd


Final_DB = pd.read_csv(
    r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.1\Albion_Webscraper.csv")

Fix_DB = pd.read_csv(
    r"C:\Users\gabri\Documents\Projects\Albion\albiondata\V1.1\Final_URLS.csv")

Complete_DB = pd.merge(Final_DB, Fix_DB, how='outer', 
                       left_on=['Product', 'Category_Name', 'Crafting_Focus',	
                                'Ingredient_1_Image', 'Ingredient_1_Name', 'Ingredient_1_Amount', 
                                'Ingredient_2_Image', 'Ingredient_2_Name', 'Ingredient_2_Amount', 
                                'Ingredient_3_Image', 'Ingredient_3_Name', 'Ingredient_3_Amount', 
                                ],
                       right_on=['Product', 'Category_Name', 'Crafting_Focus',	
                                'Ingredient_1_Image', 'Ingredient_1_Name', 'Ingredient_1_Amount', 
                                'Ingredient_2_Image', 'Ingredient_2_Name', 'Ingredient_2_Amount', 
                                'Ingredient_3_Image', 'Ingredient_3_Name', 'Ingredient_3_Amount', 
                                ]
                       )
Complete_DB.drop_duplicates(subset=['Category_Name'], inplace=True)
Complete_DB = Complete_DB.iloc[:, 1:]

Complete_DB.to_csv('Complete_DB.csv')
