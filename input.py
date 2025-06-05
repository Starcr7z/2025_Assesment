from utils import parse_amount_unit

def get_recipe_info():
    recipe_name = input("Enter the recipe name: ").strip()
    while True:
        servings_input = input("Enter the number of servings: ").strip()
        if servings_input.isdigit() and int(servings_input) > 0:
            servings = int(servings_input)
            break
        else:
            print("❌ Please enter a valid positive integer for servings.")
    return recipe_name, servings

def get_ingredient_info():
    ingredient = input("Ingredient name (or 'xxx' to finish): ").strip()
    if ingredient.lower() == 'xxx':
        return None

    # Amount used input
    while True:
        amount_used_input = input(f"Amount of {ingredient} used (e.g., 3 tbsp, 100g): ").strip()
        parsed_used = parse_amount_unit(amount_used_input)
        if parsed_used:
            amount_used, unit_used = parsed_used
            break
        else:
            print("❌ Please enter amount and unit correctly (e.g., '3 tbsp', '100g').")

    # Amount purchased input - use same unit
    while True:
        amount_purchased_input = input(f"Amount of {ingredient} purchased (e.g., 500 {unit_used}): ").strip()
        parsed_purchased = parse_amount_unit(amount_purchased_input)
        if parsed_purchased and parsed_purchased[1] == unit_used and parsed_purchased[0] > 0:
            amount_purchased, unit_purchased = parsed_purchased
            break
        else:
            print(f"❌ Please enter a positive amount with the same unit '{unit_used}'.")

    # Cost purchased input
    while True:
        cost_input = input(f"Cost of purchased amount ($): ").strip()
        try:
            cost_purchased = float(cost_input)
            if cost_purchased > 0:
                break
            else:
                print("❌ Cost must be positive.")
        except ValueError:
            print("❌ Please enter a valid number for cost.")

    return ingredient, amount_used, amount_purchased, cost_purchased
