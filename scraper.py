import pandas as pd
import numpy as np

def get_nutrients(link, name):
  data = pd.read_html(link)[1]
  data.rename(columns={'Per 100 Gram.': name}, inplace = True)
  data.rename(columns={'Per 100 Milliliter.': name}, inplace = True)
  if 'RI*' in data.columns:
    data.drop('RI*', axis = 1, inplace = True)
  data = data.transpose()
  data = data.rename(columns=data.iloc[0]).drop(data.index[0])
  return data

  # to do: scrape price from website, and make app to measure stock in realtime
links = ["https://www.ah.nl/producten/product/wi48405/ah-basic-havermout", 
         "https://www.ah.nl/producten/product/wi197393/ah-bananen",
         "https://www.ah.nl/producten/product/wi383520/ah-amandel-drink-ongezoet",
         "https://www.ah.nl/producten/product/wi4180/ah-aubergine" ,
         "https://www.ah.nl/producten/product/wi161730/ah-medjoul-dadels",
         "https://www.ah.nl/producten/product/wi167873/ah-kikkererwten-0",
         "https://www.ah.nl/producten/product/wi30428/ah-kidneybonen-0",
         "https://www.ah.nl/producten/product/wi426102/ah-ongezouten-notenmix"
         ]
names = ['oats', 'bananas', 'almond milk', 'eggplant', 'medjoul dates', 'chickpeas', 'kidney beans', 'unsalted nut mix']
stock = [100, 5, 0, 1, 1, 1, 1, 1]
prices = [0.6, 1.2, 1, 0.79, 0.95, 0, 0, 0]
portion = [60, 150, 200, 200, 24, 100, 100, 40]
prep = ['microwave', 'raw', 'raw', 'grill', 'raw', 'raw', 'raw', 'raw']
assert len(links) == len(names)
len(names)

# to do: make sure to not lose information/columns (instead place NaNs!)
data = pd.DataFrame()
for i in range(len(links)):
  data = data.append(get_nutrients(links[i], names[i]))

def split_values(table, column_to_split):
  new = table[column_to_split].str.split(" ", n = 1, expand = True) 
  table[column_to_split]= new[0] 
  table[column_to_split + " (unit)"]= new[1] 
  return table

new = data['Energie'].str.split(" ", n = 4, expand = True) 
data['Energie'] = new[2].str.slice(start=1)
data = split_values(data, "Eiwitten")
data = split_values(data, "Koolhydraten")
#data = split_values(data, "Voedingsvezel")
data = split_values(data, "Vet")
data.index.name = 'Ingredient'

data = data[['Energie', 'Vet', 'Koolhydraten', 'Eiwitten' ]]

export = data.rename(columns={'Energie': 'Calories', 'Vet': 'Total_Fat (g)', 'Koolhydraten': 'Carbohydrates (g)', 'Eiwitten': 'Protein (g)'})
export.to_excel('ingredients - scraped.xls')