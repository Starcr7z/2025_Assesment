from input import get_recipe_info, get_ingredient_info
from calculations import calculate_cost_used
from display import show_instructions, show_results

def main():
    show_instructions()
    recipe_name, servings = get_recipe_info()
    total_cost = 0
    ingredient_costs = []

    while True:
        ingredient_data = get_ingredient_info()
        if ingredient_data is None:
            break  # User entered 'xxx' to stop

        cost_used = calculate_cost_used(*ingredient_data[1:])  # pass amounts & cost
        ingredient_costs.append(cost_used)
        total_cost += cost_used
        print(f"Cost of {ingredient_data[0]} used: ${cost_used:.2f}\n")

    show_results(recipe_name, servings, total_cost)

if __name__ == "__main__":
    main()
