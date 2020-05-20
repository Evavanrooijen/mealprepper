import streamlit as st
import pandas as pd
from LP import plan_meals

st.title('Welcome to the mealprepper!')
if st.checkbox("What's this?"):
    st.write('This tool calculated the optimal recipe given a set of ingredients and the macro\
        targets for this meal. The solution will be optimal meaning it is the best possible way \
            to get as close to your carb, protein and fat targets while minimzing the total amount\
                of calories. When the list of ingredients is low, the solution might not be exact.')

kcal_target = st.sidebar.number_input('Kcal Target', 0, 1000, 600, step=10)
st.sidebar.success('Default macro split is 30% protein, 40% carbs and 30% fat, feel free to change')
protein_target = st.sidebar.number_input('Protein (g)', 0, 100, round(0.3*kcal_target/4), 1)
carbs_target = st.sidebar.number_input('Carbs (g)', 0, 200, round(0.4*kcal_target/4), 1)
fat_target = st.sidebar.number_input('Fat (g)', 0, 60, round(0.3*kcal_target/9), 1)
#fiber_target = st.sidebar.number_input('Fiber (g)', 0, 50, 30, 1)

ingredients_df = pd.read_excel('ingredients - scraped.xls')
#showcase = ['Ingredients','Calories', 'Total_Fat (g)', 'Carbohydrates (g)', 'Protein (g)']

if st.sidebar.checkbox('Show ingredients', value=True):
    meal_type = st.selectbox('Select meal type', ['All', 'Breakfast', 'Liner', 'Snacks'])
    st.write('Nutritional value per 100 gram')
    if meal_type == 'All':
        meal_df = ingredients_df
    else: meal_df = ingredients_df.loc[ingredients_df['Meal'] == meal_type]
    st.dataframe(meal_df, width=None, height=500)
if st.button('Calculate recipe'):
    st.write('Given these ingredients and the specified macro targets, the optimal recipe is:')
    for v in plan_meals(meal_df, kcal_target, protein_target, fat_target, carbs_target, deviation=0):
        if v.varValue>0:
            st.write(v.name, "=", round(v.varValue), ' grams')
