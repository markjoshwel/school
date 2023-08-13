print("Car Insurance Calculator\n" "========================")

gender: str = ""
while gender not in ["M", "F"]:
    gender = input("Enter gender [M/F]: ").upper()

age: int = -1
while age == -1:
    _age = input("Enter age: ")
    age = int(_age) if _age.isdigit() else -1

historical_accidents: str = ""
while historical_accidents not in ["Y", "N"]:
    historical_accidents = input(
        "Have you been in a traffic accident before? [Y/N] "
    ).upper()

premium_rate: float = 0.0

if gender == "M":
    if age < 25:
        premium_rate = 1.8

    elif age < 35:
        premium_rate = 1.5

    elif age < 45:
        premium_rate = 1.2

    elif age < 55:
        premium_rate = 1.0

    elif age < 64:  # using 64 as per coursemology prompt!
        premium_rate = 1.4

    else:
        premium_rate = 1.7

else:
    if age < 25:
        premium_rate = 1.4

    elif age < 35:
        premium_rate = 1.3

    elif age < 45:
        premium_rate = 1.1

    elif age < 55:
        premium_rate = 0.9

    elif age < 64:  # using 64 as per coursemology prompt!
        premium_rate = 1.2

    else:
        premium_rate = 1.4

premium_cost: float = (800 * premium_rate) + (
    300 if (historical_accidents == "Y") else 0
)

print(f"Your annual premium is: {premium_cost:.1f}")
