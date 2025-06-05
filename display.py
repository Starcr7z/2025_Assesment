def show_instructions():
    print("""
Welcome to the Recipe Cost Calculator!
You will enter ingredients one by one.
Enter 'xxx' as the ingredient name to finish.
All costs are calculated per recipe and per serving.
""")

def show_results(recipe_name, servings, total_cost):
    cost_per_serving = total_cost / servings if servings > 0 else 0
    print(f"\nRecipe: {recipe_name}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Cost per Serving: ${cost_per_serving:.2f}")
