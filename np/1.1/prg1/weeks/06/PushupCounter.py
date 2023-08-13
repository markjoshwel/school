# PushupCounter: Mark Joshwel (SXXXXXXXX)

pushup_target = int(input("Enter target number of pushups: "))
pushup_total = 0

day = 1
while pushup_total < pushup_target:
    pushup_total += int(input(f"Day {day}: How many pushups did you do today? "))
    day += 1

print(f"You did a total of {pushup_total}.")
print(f"You hit your target in {days-1} days!")
