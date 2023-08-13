# PrintCalendar
# Mark Joshwel - SXXXXXXXX

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"] * 2

ndays = int(input("Enter number of days: "))
start_day = input("When is the first day of the week: ")

print(
    """
 Sun Mon Tue Wed Thu Fri Sat"""
)

current_day = days.index(start_day)
day = 1
count = 1

for nweek in range(1, ndays + current_day + 1, 7):
    for nday in range(1, 7 + 1):
        # print(nday, current_day, count)
        if (nweek == 1) and (count < (days.index(start_day) + 1)):
            print("    ", end="")

        elif day <= ndays:
            print(f"{day}".rjust(4), end="")
            day += 1

        count += 1
        current_day += 1

    if current_day >= 7:
        current_day -= 7

    print()
