# Mark Joshwel (SXXXXXXXX) - IM02

num1, num2 = (
    int(input("Enter num1: ")),
    int(input("Enter num2: ")),
)
if num1 > num2:
    num1, num2 = num2, num1

x = int(input(f"Enter a number between {num1} and {num2}: "))
if not (num1 <= x <= num2):
    print("Invalid number entered")

else:
    skipped = 0
    for i in range(num1, num2 + 1):
        if i % x == 0:
            print(" skip")
            skipped += 1

        else:
            print(f"{i:>5}")

    print(f"{skipped} integers skipped")
