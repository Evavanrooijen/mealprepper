import streamlit as st
import pandas as pd
from LP import plan_meals
# introduce class mealplan, subclasses ingredients/food 
# contains targets, ingredients, stock

# Read the first few rows dataset in a Pandas DataFrame
# Read only the nutrition info not the bounds/constraints
df = pd.read_excel("diet - medium.xls",nrows=17)

# Create a list of the food items
food_items = list(df['Foods'])

# Create a dictinary of costs for all food items
costs = dict(zip(food_items,df['Price/Serving']))

# Create a dictionary of calories for all food items
calories = dict(zip(food_items,df['Calories']))

# Create a dictionary of total fat for all food items
fat = dict(zip(food_items,df['Total_Fat (g)']))

# Create a dictionary of carbohydrates for all food items
carbs = dict(zip(food_items,df['Carbohydrates (g)']))
fiber = dict(zip(food_items,df['Dietary_Fiber (g)']))

protein = dict(zip(food_items,df['Protein (g)']))

st.title('Welcome to the mealprepper!')
#st.write('Targets set: ' + str(targets_set))
#st.write('Plan created: ' + str(plan_made))
#st.write('Groceries bought: ' + str(groceries_bought))
#st.write('Meals prepped: ' + str(meals_prepped))

#app_mode = st.sidebar.radio('Hello World!', ['Guidelines', 'Set Targets', 'Plan Meals', 'Buy Groceries', 'Prep Foods'])

#if st.checkbox('Show weight/body fat progress'):
    #st.write('platemethod an common macro splits')
 #   st.line_chart(progress.drop('Date', axis=1))

kcal_target = st.sidebar.number_input('Kcal Target', 1000, 6000, 2500, 50)
protein_target = st.sidebar.number_input('Protein Target', 150, 300, round(0.3*kcal_target/4), 1)
carbs_target = st.sidebar.number_input('Carbs Target', 100, 500, round(0.4*kcal_target/4), 1)
fat_target = st.sidebar.number_input('Fat Target', 20, 150, round(0.3*kcal_target/9), 1)
meals = st.sidebar.number_input('Number of meals/day', 1, 6, 3)
equal_split = st.sidebar.checkbox('Spread macros evenly across all meals')
targets_set = True
bar.progress(1)
if st.button('Move on to meal planning'):
    app_mode = "Plan Meals"
    #plan_meals(kcal_inp)
    #st.sidebar.success('To continue select "Run the app".')
#if st.checkbox("Plan Meals"):
    st.write('hello, Im running')
    if targets_set == False:
        st.success('Error: Missing targets.... ')
    else:
        st.write('Planning {} meals'.format(meals))
        #Need help? Check this video/article')
            #readme_text.empty()
            #run_the_app()
if st.checkbox('test'):
    for v in plan_meals(0, 125, 30, 80, 30):
        if v.varValue>0:
            st.write(v.name, "=", round(v.varValue))
if st.checkbox("Buy Groceries"):
    st.table(foods(foods['plan']>foods(['stock'])))
if st.checkbox('Prep Foods'):
    for food in foods:
        st.table(pd.DataFrame(columns=['method', 'amount', 'time']))# sort by time/method, sum by ingredient
        #add checkbox inside table?