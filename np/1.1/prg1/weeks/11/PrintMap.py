# Print Map
# Mark Joshwel - SXXXXXXXX

map = [
    ["T", " ", " ", " ", "T"],
    [" ", "P", " ", " ", " "],
    [" ", " ", " ", "T", " "],
    [" ", "T", " ", " ", " "],
]

for row in map:
    print("+---" * len(row), "+", sep="")
    for col in row:
        print(f"| {col} ", end="")
    print("|")

print("+---" * len(row), "+", sep="")
