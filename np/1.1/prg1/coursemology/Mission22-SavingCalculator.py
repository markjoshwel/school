# imports
from math import pow, log

R_ANNUAL_INTEREST_RATE = 0.05
N_COMPOUND_TIMES = 12

# inputs
P_init_amt = float(input("Enter the initial saving: "))
A_final_amt = float(input("Enter the final amount: "))

# processes
t = log(A_final_amt / P_init_amt) / (
    N_COMPOUND_TIMES * log(1 + (R_ANNUAL_INTEREST_RATE / N_COMPOUND_TIMES))
)

# ouputs
print(
    f"Assuming an annual, monthly-compounded interest rate of {R_ANNUAL_INTEREST_RATE * 100}%,"
    f" the number of years needed to reach the final amount is {t:.2f}"
)
