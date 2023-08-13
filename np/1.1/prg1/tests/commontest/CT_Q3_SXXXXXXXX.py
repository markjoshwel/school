# Mark Joshwel (SXXXXXXXX) - IM02

nbooks = int(input("Please enter the number of books that are late: "))
ndays = int(input("Please enter the number of days the books are late: "))

fine = 0.00

if ndays == 1:
    if nbooks == 1:
        fine = 1.20

    else:
        fine = (0.15 * nbooks) + 1.20

else:  # >= 1
    if nbooks == 1:
        fine = 2 ** (ndays - 1) * (0.3) + 1

    else:
        fine = ((2**ndays) * (0.15 * nbooks)) + 1.20

print(f"The fine for {nbooks} book(s) for {ndays} day(s) is ${fine:.2f}")
