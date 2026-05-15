def fractional_knapsack(items, capacity):
    """
    Return greedy selections for the fractional knapsack problem.
    Each item is (name, value, weight).
    """
    ordered = sorted(items, key=lambda item: item[1] / item[2], reverse=True)
    remaining_capacity = capacity
    taken = []
    total_value = 0.0

    for name, value, weight in ordered:
        if remaining_capacity == 0:
            break

        fraction = min(1, remaining_capacity / weight)
        taken_value = value * fraction
        taken_weight = weight * fraction

        taken.append((name, fraction, taken_value, taken_weight))
        total_value += taken_value
        remaining_capacity -= taken_weight

    return taken, total_value


if __name__ == "__main__":
    sample_items = [
        ("Gold", 60, 10),
        ("Silver", 100, 20),
        ("Bronze", 120, 30),
    ]
    capacity = 50

    selections, total = fractional_knapsack(sample_items, capacity)

    print("Capacity:", capacity)
    print("Selections:")
    for name, fraction, value, weight in selections:
        print(
            f"{name}: fraction={fraction:.2f}, "
            f"value_added={value:.2f}, weight_used={weight:.2f}"
        )

    print("Total value:", f"{total:.2f}")
