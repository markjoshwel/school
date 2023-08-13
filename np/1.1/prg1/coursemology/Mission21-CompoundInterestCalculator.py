# psuedocode
# ==========
# - Assign variable P the value 10000
# - Assign variable r the value 0.08
# - Assign variable n the value 12
# - Prompt user for number of years the money will be compounded as a whole number
# - Get t
# - Calculate A = P * (1 + (r / n))^(n * t)
# - Display A
#
# # Note: I'm following the template naming the principal amount 'P'

# python
# ======
P, r, n = 10000, 0.08, 12

# inputs
t = int(input("Enter number of years the money will be compounded as a whole number: "))

# process
A = P * (1 + (r / n)) ** (n * t)

# outputs
print(f"Final amount after {t} is ${A:.2f}")
