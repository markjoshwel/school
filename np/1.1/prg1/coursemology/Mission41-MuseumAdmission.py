def calculate_cost(total_no_visitors, num_SC_PR):
    if total_no_visitors == num_SC_PR:
        print("Admission is free for all.")
        return 0

    total_cost = (total_no_visitors - num_SC_PR) * 15
    print(f"Total cost is ${total_cost:.2f}")
    return total_cost


# total_no_visitors = int(input("Enter total number of visitors: "))
# num_SC_PR = int(input("Enter total number of visitors: "))
# total_cost = calculate_cost(total_no_visitors, num_SC_PR)
# print(total_cost)
