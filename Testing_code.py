def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")
    print()
    print("Enter 'xxx' when you're done entering ingredients.")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter full word or first n letters from valid answers"""
    while True:
        response = input(question).lower()
        for item in valid_answers:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")
    print('''
This program helps you calculate the total cost of a recipe.

For each ingredient, enter:
- The name of the ingredient
- The amount required for the recipe (in grams, ml, units, tbsp, or tsp)
- The amount purchased and its cost (e.g., 500 g for $4.00)

The program calculates the cost of the amount used
and totals the cost of all ingredients.

To stop adding ingredients, enter 'xxx' for the ingredient name.
''')


def convert_to_base(amount, unit):
    unit = unit.lower().strip()
    if unit in ['g', 'gram', 'grams']:
        return amount  # grams as is
    elif unit in ['ml', 'milliliter', 'milliliters']:
        return amount  # ml as is
    elif unit in ['tbsp', 'tablespoon', 'tablespoons']:
        return amount * 15  # tbsp → ml
    elif unit in ['tsp', 'teaspoon', 'teaspoons']:
        return amount * 5   # tsp → ml
    elif unit in ['unit', 'units']:
        return amount  # units as is
    else:
        return None


def get_amount_and_unit(prompt):
    """Gets amount and unit from user input like '3 tbsp' or '100 g'"""
    while True:
        user_input = input(prompt).strip().lower()
        parts = user_input.split()

        if len(parts) == 2:
            try:
                amount = float(parts[0])
                unit = parts[1]
                converted = convert_to_base(amount, unit)
                if converted is None:
                    print("❌ Unknown unit. Use g, ml, tbsp, tsp, or units.")
                    continue
                if converted <= 0:
                    print("❌ Amount must be positive.")
                    continue
                return converted, unit
            except ValueError:
                print("❌ Invalid amount. Enter number and unit (e.g. '2 tbsp').")
        else:
            print("❌ Please enter amount and unit, like '3 tbsp' or '100 g'.")


def get_positive_int(prompt):
    """Asks for a positive integer >= 1"""
    while True:
        response = input(prompt).strip()
        if response.isdigit():
            val = int(response)
            if val >= 1:
                return val
            else:
                print("❌ Number must be 1 or greater.")
        else:
            print("❌ Please enter a valid positive whole number.")


def calculate_cost_with_units():
    total_cost = 0
    ingredient_num = 1

    while True:
        ingredient = input(f"📝 Ingredient #{ingredient_num} name: ").strip()
        if ingredient.lower() == 'xxx':
            break

        amount_used, used_unit = get_amount_and_unit(
            f"📏 Amount of {ingredient} used in recipe (e.g., 2 tbsp, 100 g, 50 ml): "
        )

        # When asking amount purchased, only ask for number,
        # and use same unit as amount_used
        while True:
            purchased_input = input(
                f"📦 Amount of {ingredient} purchased (in {used_unit}): "
            ).strip()

            try:
                amount_purchased = float(purchased_input)
                if amount_purchased <= 0:
                    print("❌ Amount purchased must be positive.")
                    continue
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            # Check that amount used <= amount purchased
            if amount_used > amount_purchased:
                print("⚠️ You cannot use more than you purchased. Try again.")
                continue

            break

        while True:
            try:
                cost_purchased = float(input(f"💵 Cost of purchased amount ($): ").strip())
                if cost_purchased < 0:
                    print("❌ Cost cannot be negative.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        cost_used = (amount_used / amount_purchased) * cost_purchased
        total_cost += cost_used

        print(f"✅ Cost of {amount_used} {used_unit} from {ingredient}: ${cost_used:.2f}\n")
        ingredient_num += 1

    return total_cost


# --- Main routine ---

make_statement("Recipe Cost Calculator", "💲")

print()
if string_check("Do you want to see the instructions? ") == "yes":
    instructions()

print()

# Get recipe name (cannot be blank)
while True:
    recipe_name = input("🍳 Enter the recipe name: ").strip()
    if recipe_name:
        break
    print("❌ Recipe name cannot be blank.")

# Get number of servings (positive integer)
servings = get_positive_int("🍽️ How many servings does this recipe make? ")

print()

# Calculate total cost
total_cost = calculate_cost_with_units()

if servings > 0:
    cost_per_serving = total_cost / servings
else:
    cost_per_serving = 0

print(f"\n🍰 Recipe: {recipe_name}")
print(f"👥 Servings: {servings}")
print(f"💰 Total recipe cost: ${total_cost:.2f}")
print(f"🧾 Cost per serving: ${cost_per_serving:.2f}")
