def calculate_average(mthly_cost: str) -> float:
    mthly_cost_list = [float(c) for c in mthly_cost.split(";")]
    average = sum(mthly_cost_list) / len(mthly_cost_list)
    return average


# mthly_cost = input("Enter the electrical cost ($) for 3 months seperated by semicolon: ")
# average = calculate_average(mthly_cost)
# print(f"Average electrical cost($): {average}")
