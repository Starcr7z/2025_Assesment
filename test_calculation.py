from calculations import calculate_cost_used

def test_calculate_cost_used():
    cost = calculate_cost_used('sugar', 50, 500, 4.0)
    assert abs(cost - 0.4) < 1e-6, "Calculation error for sugar cost"
    print("Calculation test passed.")

test_calculate_cost_used()
