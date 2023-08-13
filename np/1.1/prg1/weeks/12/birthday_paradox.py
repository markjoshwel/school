# Birthday Paradox
# Mark Joshwel (SXXXXXXXX - IM02/P12)

from random import randint


def paradox():
    birthdays = []
    tries = 0

    while True:
        bday = randint(1, 365)
        print(f"{bday} was randomly generated.")
        if bday in birthdays:
            break

        birthdays.append(bday)
        tries += 1

    print(f"Duplicate day! This took {tries} tries.")


print("This program demonstartes the birthday paradox.")
paradox()
