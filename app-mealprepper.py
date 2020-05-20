import streamlit as st
import pandas as pd

# introduce class mealplan, subclasses ingredients/food 
# contains targets, ingredients, stock

@st.cache
def plan_meals(targets, foods):
    return None

@st.cache
def set_targets(kcal, protein, carbs, fat, fiber, meals):
    return None

@st.cache
def grocery_list(ingredients):
    # for item in ingredients
    # if stock< xi*1, 1 
    # add to grocery list
    return None

a = 5
targets_set = False
plan_made = False
groceries_bought = False
meals_prepped = False

bar = st.progress(0)

st.title('Welcome to the mealprepper!')
#st.write('Targets set: ' + str(targets_set))
#st.write('Plan created: ' + str(plan_made))
#st.write('Groceries bought: ' + str(groceries_bought))
#st.write('Meals prepped: ' + str(meals_prepped))
if targets_set & plan_made & groceries_bought & meals_prepped:
    st.sidebar.success('All set! Ready to make some gains!!')

progress = pd.read_csv('progress.csv', delimiter = ';')

app_mode = st.sidebar.radio('Hello World!', ['Guidelines', 'Set Targets', 'Plan Meals', 'Buy Groceries', 'Prep Foods'])

if app_mode == "Guidelines":
    #st.write('platemethod an common macro splits')
    st.line_chart(progress.drop('Date', axis=1))
elif app_mode == "Set Targets":
    kcal_target = st.number_input('Kcal Target', 1000, 6000, 2500, 50)
    protein_target = st.number_input('Protein Target', 150, 300, round(0.3*kcal_target/4), 1)
    carbs_target = st.number_input('Carbs Target', 100, 500, round(0.4*kcal_target/4), 1)
    fat_target = st.number_input('Fat Target', 20, 150, round(0.3*kcal_target/9), 1)

    meals = st.number_input('Number of meals/day', 1, 6, 3)
    equal_split = st.checkbox('Spread macros evenly across all meals')
    targets_set = True
    bar.progress(1)
    if st.button('Move on to meal planning'):
        app_mode = "Plan Meals"
        #plan_meals(kcal_inp)
    #st.sidebar.success('To continue select "Run the app".')
elif app_mode == "Plan Meals":
    st.write('hello, Im running')
    if targets_set == False:
        st.success('Error: Missing targets.... ')
    else:
        st.write('Planning {} meals'.format(meals))
        #Need help? Check this video/article')
            #readme_text.empty()
            #run_the_app()
elif app_mode == "Buy Groceries":
    st.table(foods(foods['plan']>foods(['stock'])))
elif app_mode == "Prep Foods":
    for food in foods:
        st.table(pd.DataFrame(columns=['method', 'amount', 'time']))# sort by time/method, sum by ingredient
        #add checkbox inside table?