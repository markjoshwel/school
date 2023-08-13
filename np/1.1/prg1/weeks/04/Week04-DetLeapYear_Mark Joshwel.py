year = int(input("Please enter the year: "))

print(
    year,
    "is a leap year."
    if ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)))
    else "is not a leap year.",
)
