# Mark Joshwel (SXXXXXXXX) - IM02

tn = int(input("Enter a number between 0 and 5000: "))

for n in range(1, 101):  # Tn(100) = 5050
    _tn = ((n**2) + n) / 2
    if tn == _tn:
        print(f"{tn} is a triangular number and is the {n}th number.")
        break

else:
    print(f"{tn} is NOT a triangular number.")
