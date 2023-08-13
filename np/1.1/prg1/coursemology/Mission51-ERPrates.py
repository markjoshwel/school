def calculate_card_value(card_value, time_of_entry):
    erp_rate = 0.00
    successful_deduction = False

    if 12.00 <= time_of_entry < 17.30:
        erp_rate = 0.50

    elif time_of_entry <= 17.35:
        erp_rate = 1.00

    elif time_of_entry <= 18.00:
        erp_rate = 1.50

    elif time_of_entry <= 18.55:
        erp_rate = 2.00

    elif time_of_entry <= 19.00:
        erp_rate = 1.50

    elif time_of_entry <= 19.55:
        erp_rate = 1.00

    elif time_of_entry < 20.00:  # WRONG
        erp_rate = 0.50

    else:
        erp_rate = 0

    print(f"The ERP is ${erp_rate:.2f}")

    if erp_rate > 0:
        if card_value < erp_rate:
            print(
                "You do not have enough balance in your card to pay for the ERP charge.\n"
                "The amount is not deducted, you have to pay a fine for this"
            )

        else:
            card_value -= erp_rate
            successful_deduction = True

    return [erp_rate, card_value, successful_deduction]


# card_value = float(input("Please enter the current value in cash card : $"))
# time_of_entry = float(input("Please eter time at ERP gantry : "))

# erp_rate, card_value, successful_deduction = calculate_card_value(
#     card_value, time_of_entry
# )

# if successful_deduction:
#     print("The amount is deducted successfully")

# print(f"Your card value is ${card_value:.2f}")
