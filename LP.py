# min costs
# st. kcal, protein, carbs, fats, fiber

# returns xi for every ingredient

from pulp import *
import pandas as pd

def plan_meals(df, kcal_target, protein_target, fat_target, carb_target, deviation=5):
    deviation = deviation/100 + 1
    
    # Create a list of the food items
    food_items = list(df['Ingredient'])

    # Create a dictinary of costs for all food items
    # costs = dict(zip(food_items,df['Price/Serving']))

    # Create a dictionary of calories for all food items
    calories = dict(zip(food_items,df['Calories']/100))
    
    # Create a dictionary of total fat for all food items
    fat = dict(zip(food_items,df['Total_Fat (g)']/100))

    # Create a dictionary of carbohydrates for all food items
    carbs = dict(zip(food_items,df['Carbohydrates (g)']/100))
    # fiber = dict(zip(food_items,df['Dietary_Fiber (g)']))

    protein = dict(zip(food_items,df['Protein (g)']/100))

    prob = LpProblem("mealplanner", LpMinimize)
    food_vars = LpVariable.dicts("Amount",food_items,lowBound=0,cat='Continuous') #integer, creates food_vars+food_items key
    prob += lpSum([calories[i]*food_vars[i] for i in food_items]) #objective

    # Fat
    prob += lpSum([fat[f] * food_vars[f] for f in food_items]) >= fat_target/deviation, "FatMinimum"
    prob += lpSum([fat[f] * food_vars[f] for f in food_items]) <= fat_target*deviation, "FatMaximum"

    # Carbs
    prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) >= carb_target/deviation, "CarbsMinimum"
    prob += lpSum([carbs[f] * food_vars[f] for f in food_items]) <= carb_target*deviation, "CarbsMaximum"

    # Fiber
    #prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) >= fiber_target/deviation, "FiberMinimum"
    #prob += lpSum([fiber[f] * food_vars[f] for f in food_items]) <= fiber_target*deviation, "FiberMaximum"

    # Protein
    prob += lpSum([protein[f] * food_vars[f] for f in food_items]) >= protein_target/deviation, "ProteinMinimum"
    prob += lpSum([protein[f] * food_vars[f] for f in food_items]) <= protein_target*deviation, "ProteinMaximum"

    prob.solve()
    return prob.variables()
