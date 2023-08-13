# Square of Characters
# Mark Joshwel (SXXXXXXXX - IM02/P12)


def print_square(side: int, char: str):
    for _ in range(side):
        print(f"{char} " * side)


side = int(input("Enter side of square as an integer: "))
char = input("Enter character to be used: ")
print_square(side, char)
