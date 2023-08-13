# psuedocode
# ==========
# - Prompt user for number of 50 cents as a whole number
# - Get cent50
# - Prompt user for number of 20 cents as a whole number
# - Get cent20
# - Prompt user for number of 10 cents as a whole number
# - Get cent10
# - Prompt user for number of 5 cents as a whole number
# - Get cent5
# - Calculate total = (cent50 * 0.50) + (cent20 * 0.20) + (cent10 * 0.10) + (cent5 * 0.05)
# - Display total

# python
# ======
# inputs
cent20 = int(input("Enter nu.mber of 50 cents as a whole number: "))
cent50 = int(input("Enter number of 20 cents as a whole number: "))
cent10 = int(input("Enter number of 10 cents as a whole number: "))
cent5 = int(input("Enter number of 5 cents as a whole number:  "))

# process
total = (cent50 * 0.50) + (cent20 * 0.20) + (cent10 * 0.10) + (cent5 * 0.05)

# output
print(f"Your total is {total:.2f}.")
