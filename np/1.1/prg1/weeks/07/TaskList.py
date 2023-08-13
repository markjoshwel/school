# TaskList: Mark Joshwel (SXXXXXXXX)
ndays = int(input(f"Enter number of days: "))

for wkd in range(1, ndays + 1, 7):
    print("Day | Task(s)")
    for day in range(wkd, min(wkd + 7, ndays + 1)):
        print(f"{day:>3} |")
