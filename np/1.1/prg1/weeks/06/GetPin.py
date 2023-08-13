# GetPin: Mark Joshwel (SXXXXXXXX)

pin = "123"
tries = 2

guess = input("Enter pin: ")
while (tries != 0) and (guess != pin):
    print("Invalid pin. Please try again.\n" f"You have {tries} tries left.")
    guess = input("Enter pin: ")
    tries -= 1

if tries == 0:
    print("Invalid pin. You have no more tries.\nYour account is locked.")
else:
    print("Valid pin!")
