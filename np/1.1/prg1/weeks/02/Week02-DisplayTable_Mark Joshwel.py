from math import sqrt

numbers_literal = [1, 2, 3, 4, 5]
numbers_english = ["One", "Two", "Three", "Four", "Five"]

print("Number  Square  Square root  English")
for literal, english in zip(numbers_literal, numbers_english):
    print(f"{literal:>6}  {literal ** 2:^6}  {sqrt(literal):^11.2f}  {english:>7}")
