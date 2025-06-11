def show_instructions():
    print('''

This program helps you calculate the total cost of a recipe.

For each ingredient, enter:
- The name of the ingredient
- The amount required for the recipe (in grams, ml, or units)
- The amount purchased and its cost (e.g., 500g for $4.00)

The program will calculate the cost of the amount used
in the recipe, and at the end, it will total the cost
of all ingredients.

To stop adding ingredients, enter the exit code ('xxx') 
when prompted for the ingredient name.

    ''')

def show_results(recipe_name, servings, total_cost):
    cost_per_serving = total_cost / servings if servings > 0 else 0
    print(f"\nRecipe: {recipe_name}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Cost per Serving: ${cost_per_serving:.2f}")
