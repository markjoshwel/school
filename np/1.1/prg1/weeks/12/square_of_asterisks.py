# Square of Asterisks
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def print_square(side: int):
    for _ in range(side):
        print("* " * side)


side = int(input("Enter side of square as an integer: "))
print_square(side)
