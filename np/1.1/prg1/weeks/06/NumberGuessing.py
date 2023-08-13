# NumberGuessing: Mark Joshwel (SXXXXXXXX)

from random import randint

tries = 5
num = randint(1, 100)
guess = 0

print("Welome to Number Guessing Game")
i = 1
while guess != num:
    if i > tries:
        print(f"You couldn't guess it within {tries} tries!")
        break

    guess = int(
        input(
            f"Try {i}: Enter a number between 1 and 100 (or -1 to end): "
            if (i == 1)
            else f"Try {i}: Guess again, enter a number between 1 and 100 (or -1 to end): "
        )
    )

    if guess == -1:
        break
    elif guess > num:
        print(f"{guess} is too high.")
    elif guess < num:
        print(f"{guess} is too low.")

    i += 1

else:
    print("Bingo, you've got it right!")

print("\nBye-bye!")
