from scraper import *
import pandas as pd

link = ['https://www.ah.nl/producten/product/wi48405/ah-basic-havermout', 'https://www.ah.nl/producten/product/wi383520/ah-amandel-drink-ongezoet']
name = ['oats', 'almond milk'] 
portion = [60, 200]

for idx in range(len(link)):
    get_nutrients(link[idx], name[idx])

foods = pd.append(get_nutrients(link, name), foods)
foods.to_csv('foods.csv')

#meal 1 oats
# meal 2 chicken and veg


# introduce class mealplan, subclasses ingredients/food, contains targets, ingredients, stock