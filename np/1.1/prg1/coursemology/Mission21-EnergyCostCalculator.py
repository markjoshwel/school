# psuedocode
# ==========
# - Prompt user for power rating of device in watts as a whole number
# - Get power_rating
# - Prompt user for number of hours used per day as a whole number
# - Get hours
# - Calculate cost = (30 * (power_rating * hours) / 1000) * 0.27543)
# - Display cost

# python
# ======
# inputs
power_rating = int(
    input("Enter the power rating of device in watts as a whole number: ")
)
hours = int(input("Enter the number of hours used per day as a whole number: "))

# process
daily_consumption = (power_rating * hours) / 1000
monthly_consumption = daily_consumption * 30  # 30 days in April 2023
cost = monthly_consumption * 0.27543  # tariff as of April 2023

# output
print(f"Monthly electricity consumption cost: ${cost:.2f}.")
