# Mark Joshwel (SXXXXXXXX) - IM02

require_var = input("Do you require toppings? [Yes / No]: ")  # error 6
toppings_set_var = int(input("Portions of toppings required: "))  # error 7
loyalty_var = input("Do you have the 'loyalty' card? [Yes / No]: ")  # error 1, 2

total_cost = 2.50  # error 3

if require_var.capitalize() == "Yes":  # error 8
    total_cost = (1.2 * toppings_set_var) + total_cost  # error 9

if loyalty_var.capitalize() == "Yes":  # error 4
    total_cost *= 0.9  # error 5

print("Total cost: ${:.2f}".format(total_cost))  # error 10


# good

"""
Overall Grade : A+
 /\_/\      /\_/\  
(=^ .^=)   (=^ .^=)
 c   "   c   c   "   c
"""
